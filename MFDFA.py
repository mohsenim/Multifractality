import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from numpy.lib.stride_tricks import as_strided
from numpy.polynomial.polynomial import polyval, polyfit


def compute_profile(X):
    '''
    Computes profile of X.
    '''

    return np.cumsum(X - np.mean(X))


def windowing(X, s):
    '''
    Makes a sliding-window view of X.
    '''
    
    if not X.flags['C_CONTIGUOUS']:
        X = X.copy()
    return as_strided(X, (X.shape[0] // s, s), ((s * X.dtype.itemsize), X.dtype.itemsize))
    

def bidir_mean_variance(X, scales, m=1):
    '''
    Computes the mean square fluctuation of residuals in sliding windows. Once from the beginning and once from the end.
    '''
    out = np.empty((len(scales), 2 * X.shape[0] // scales[0]))
    out[:] = np.nan
    X_inverse = X[::-1]
    for j, scale in enumerate(scales):
        idx = int((out.shape[1] // 2) - (X.shape[0] // scale))
        Y = np.concatenate((windowing(X, scale), windowing(X_inverse, scale)))
        i = np.arange(scale)
        coef = polyfit(i, Y.T, m)
        var = np.mean((Y - polyval(i, coef)) ** 2, axis=1)
        out[j, idx:idx + var.shape[0]] = var
    return out


def compute_fluctuation_function(mv, qs):
    '''
    Compute scaling function F
    '''
    out = np.zeros((mv.shape[0], len(qs)), 'f8')
    mv = np.nan_to_num(mv)
    mask = mv < 0.0005  ## <0.0005 filters small values
    maskedMV = np.ma.array(mv, mask=mask, dtype=np.float64)
    for qi, q in enumerate(qs):
        if q == 0:
            continue
        out[:, qi] = (maskedMV ** (q / 2)).mean(1) ** (1.0 / q)
    out[:, qs == 0] = np.exp(0.5 * (np.ma.log(maskedMV)).mean(1))[:, None]
    return out



def MFDFA_algorithm(series, scales, qs, polynomial_order=1):
    '''
    Applies MFDFA on a series
    '''
    profile = compute_profile(series)
    bmv = bidir_mean_variance(profile, scales, m=polynomial_order)
    Fq = compute_fluctuation_function(bmv, qs)
    Hq = np.zeros(len(qs))
    polynomial_coeff = np.zeros((len(qs), polynomial_order + 1))  # coefficients of fitted lines
    LSE = np.zeros(len(qs))  # least square error
    R2 = np.zeros(len(qs))  # R^2: goodness of fit
    for qi, q in enumerate(qs):
        try:
            mask = Fq[:, qi]==0
            mScales = np.ma.array(scales, mask=mask)
            mFq = np.ma.array(Fq[:, qi], mask=mask)
            coefs = np.ma.polyfit(np.ma.log2(mScales), np.ma.log2(mFq), 1)
            polynomial_coeff[qi] = coefs
            LSE[qi] = mean_squared_error(np.log2(mFq[mFq.mask==False]), np.polyval(coefs, np.log2(mScales[mScales.mask==False])))
            R2[qi] = r2_score(np.log2(mFq[mFq.mask==False]), np.polyval(coefs, np.log2(mScales[mScales.mask==False])))
            Hq[qi] = coefs[0]
        except:
            Hq[qi] = 0.5

    tq = Hq * qs - 1
    hq = np.diff(tq) / (qs[1] - qs[0])
    Dq = (qs[:-1] * hq) - tq[:-1]

    multifractal_dimension = max(hq) - min(hq)
    alfa0 = Hq[qs == 0][0]
    asymmetry = ((max(hq) - alfa0) - (alfa0 - min(hq))) / multifractal_dimension

    result = dict()
    result['series'] = series
    result['scales'] = scales
    result['qs'] = qs
    result['scaling_function'] = Fq
    result['h_q'] = Hq
    result['polynomial_coeff'] = polynomial_coeff
    result['H'] = result['h_q'][qs==2][0]
    result['tq'] = tq
    result['hq'] = hq
    result['Dq'] = Dq
    result['LSE'] = LSE
    result['R2'] = R2
    result['multifractality'] = multifractal_dimension
    result['asymmetry'] = asymmetry
    
    return result


def get_scales(length):
    '''
    Returns the list of window sizes according to the length of the series. scales=16, 24, 32,...,(length/scale)>=3
    '''
    scales = []
    n = 6
    while 2 ** np.floor(n / 2.) + 2 ** np.floor((n + 1.) / 2.) < length / 3:
        scales.append(2 ** np.floor(n / 2.) + 2 ** np.floor((n + 1.) / 2.))
        n += 1
    scales = np.array(scales).astype('i4')
    return scales


def MFDFA(series):
    '''
    Returns three fractal metrics: degree of fractality, degree of multifractality, and asymmetry.
    MFDFA_algorithm returns more metrics and values. If you need them you should
    :param series:
    :return:
    '''
    scales = get_scales(series.size)
    qs = np.arange(-5.0, 5.01, 1.0 / 4)
    result = MFDFA_algorithm(series, scales, qs, 1)
    return result
    

if __name__ == "__main__":
#   The sample text, A Christmas Carol by Charles Dickens, is POS-tagged and the nubmer of nouns in windows of 20 words is counted along the text.
    sample = np.loadtxt('./examples/Henry-James_The-Golden-Bowl.txt')
    result = MFDFA(sample)
    features = {'H': result['H'], 'multifractality': result['multifractality'], 'asymmetry': result['asymmetry']}
    print('H: {:.2f}, Multifractality: {:.2f}, Asymmetry: {:.2f} '.format(features['H'], features['multifractality'], features['asymmetry']))
