# Fractality and Long-Range Correlations
Fractality are a characteristic of a complex system in which self-similarity at different scales can be found. Fractality quantifies dynamically fluctuating variability of systems through multi-scale analyses and provides insights into underlying structures of objects under study. 

Probably the most widely used methods to analyze fractality and long-range correlations are Detrended Fluctuation Analysis (DFA; Peng et al., 1994) and Multi-Fractal Detrended Fluctuation Analysis (MFDFA; Kantelhardt et al., 2002), which is an extension of DFA. 

# Multi-Fractal Detrended Fluctuation Analysis (MFDFA)
In what follows, I outline the MFDFA procedure, according to _Kantelhardt et al., 2002_, followed by a detailed account of each step and an elaboration on how multifractal characteristics are computed. 
 
Given a series $X = x(1), x(2), \cdots, x(N)$, MFDFA processes the series as follows: 

1-	  Build the profile of the series by subtracting the mean and computing the cumulative sum:    
$$Y(i) = \sum_{k=1}^{i} [x(k) - \langle X\rangle], i=1, \cdots, N$$
    
in which $\langle X\rangle$ is the mean of $X$.
    
2-	  Divide the profile of the series into $N_s=N/s$ windows for different values of $s$, which is the size of windows.
    As the length of the series, $N$, may not be always divisible by $s$ and a portion of the series in the end may be excluded from the computation, the windowing procedure is repeated starting from the end. As a result, the number of windows increases to $2 \times N_s$.

3-	 Detrend the values in each window $v$, $v=1,\cdots,2\times N_s$, by subtracting the best fitting line, $Y'$, and calculate the mean square fluctuation of residuals:
$$F^2(s, v)=\frac{1}{s}\sum_{i=1}^{s}[Y(s \times (v-1) + i)-Y'(s \times (v-1) + i)]^2$$

4-	 Calculate the $q$th order of the mean square fluctuations:
$$F_q(s) = \{\frac{1}{2\times N_s}\sum_{v=1}^{N_s}[F^2(s, v)]^{q/2}\}^{1/q}$$
	
5-	 Compute the growth factor of fluctuations, $h(q)$, using a log-log regression on $F_q(s)$ values, i.e. $\log F_q(s)\sim h(q) \times \log s$


## Creation and Segmentation of the Profile of Series
The procedure of MFDFA is based on a random walk, which is a mathematical random process to model dynamics of systems. In a random walk, the variance of the process is time-dependent and it increases as more steps are taken. 

For illustration, suppose that an integer variable is initially set to 0 and its value increases or decreases by 1 point, i.e. either +1 or -1, according to a probability model. One can compute the mean and the variance of the values at each step.  If the model has no preference for either direction, neither increase nor decrease, the expected value of the variable, i.e. the mean, remains fixed at zero. However, the variance of the values increases proportional to the number of increases and decreases.
This implies that the standard deviation increases at a rate of the square root of the number of increases and decreases as standard deviation is the square root of variance. Consequently, the scaling factor of such a process, which exhibits no long-range correlations, is computed at 0.5. 
This behavior is typical of white noise, which exhibits no long-range correlations.

If a system has some persistency and chooses values similar to its recent choices, the scaling factor increases, indicating the presence of long-range correlations in the series of the values. 
In this so-called persistent system, the big events tend to be succeeded by big events, while small events are more likely followed by small events.
In the opposite case, if a system shows an anti-persistent behavior, the standard deviation of the series drops to values below 0.5.
In an anti-persistent system, there is a higher probability that small events follow big events than following small events, and vice versa. 

As a real example from the field of text processing, suppose that we measure lengths of sentences in a text in terms of the number of tokens. If the length of a sentence is independent from the length of preceding sentences, the sentence length series exhibits no long-range correlations, resulting in a scaling factor of 0.5. 
However, if longer (shorter) sentences tend to be followed by longer (shorter) sentences, the sentence length series is persistent, which indicates the presence of long-range correlations in the series and, as a result, the scaling factor is > 0.5. Conversely, if there is a higher likelihood of longer (shorter) sentences to follow shorter (longer) sentences, the series is anti-persistent. In this case, the scaling factor is < 0.5.

In the first step of the MFDFA procedure, where the profile of the series is created, the series is converted into a random walk. 

According to the preceding discussion, we are interested to measure the growth rate of the standard deviation as the length of the series increases. This is why the profile of the series goes into the windowing procedure in step 2 in order to compare the standard variation of sub-sequences of different sizes with each other.

## Detrending
In step 3, the sequence is first detrended by subtracting the best linear fit in each window before calculating the amount of dispersion in that window. 
A trend is an imposed changes to a system that is not raised from the intrinsic properties of the system but rather external factors. This undesired variation may affect statistics of observations, such as variance. It is not trivial to determine the source of trends in a complex system. Nevertheless, we can speculatively formulate some guesses depending on the type of data we are analyzing.
As an example from the field of text processing, if some specific structure is commonly used in a specific genre, variations in distributional text properties may not be the result of the author's choice, but rather dictated by requirements of the genre. 
As another example, suppose an author decides which discourse modes to use and how to switch between them.  Although the author has control over how to utilize discourse modes, nevertheless, alterations to distributional text properties are not completely within the author's control as distributions of syntactic word classes necessarily differ for various discourse modes.

In step 3, what remains after detrending are residuals, which are entered into the computation instead of the initial values.  However, it is expected that if the data exhibits no discernible trend, the mean square fluctuations of the initial profile values and those of the residuals are closely similar.  Note that it is possible to detrend the sequence using polynomial fits, in case a system is under influence of more complex trends.

The mean square fluctuations, which are calculated in step 3, resemble the mean variance of windows with specific size. Recall from the outset of our discussion that our goal is to determine the growth rate of fluctuations, which is directly proportional to the number of steps in a random walk. That is why, after creation of the profile of the series and segmentation of it into windows the mean square fluctuations for windows of different sizes are calculated and compared in the following steps. 

## Multiple Scaling Factors and Multifractality
The difference between DFA and MFDFA lies in steps 4 and 5. In DFA only one growth factor is calculated for a time series. However, the long-range correlation paradigm of a time series may be too complex to be explained by a single value.  _Kantelhardt et al., 2002_ thus proposed MFDFA as an extension to DFA in order to capture various scaling patterns by calculating the $q$th order of the mean square fluctuations.
Let us focus first on $q=2$. This setting turns in step 4 to a form, which resembles the mean standard deviation for windows with size $s$. This is in fact the scaling factor, which is computed by DFA.
The resulting exponent in step 5, $h(2)$, is an important measure in fractal analysis. It equals to the Hurst Exponent for stationary series.

By changing the value of $q$, the procedure puts emphasis on larger or smaller fluctuations. If $q>2$, it accentuates larger values, while if $q<2$, it emphasizes smaller variations. Given $q$, the scaling factor, $h(q)$, is calculated by fitting a line to the log-log plot of $F_q(s)$ in step 5. If the series is multifractal, fluctuations are heterogeneous and $h(q)$ varies depending on its parameter, $q$. However, if fluctuations are homogeneous, changing the value of $q$ results in no difference in scaling factors (for more discussion, see, Roeske et al., 2018). 

## Singularity Spectrum
Once scaling factors are computed, we need a way to represent the multifractality of a series. The singularity spectrum, $f(\alpha)$, summarizes multifractality information of a series effectively and lends itself to an elegant visualization. It is computed as:
$$\alpha=h(q)+qh'(q)$$
$$f(\alpha)=q[\alpha-h(q)]+1$$     

The width of the singularity spectrum, $D=\alpha_{max}-\alpha_{min}$, shows the _degree of multifractality_ of a series (for more technical details, cf.,  Kantelhardt et al., 2002). 
$\alpha_{min}$ and $\alpha_{max}$ denote the leftmost side and the rightmost side of $f(\alpha)$, respectively. If $h(q), \forall q$ are in close proximity to each other, the singularity spectrum is narrow and the series is regarded to be monofractal. In the case of multifractal series, the width of the singularity spectrum expands.

## Fractal Asymmetry
The multifractality of series may incline more toward either small or large quantities, leading to a skewness in the singularity spectrum, which can be measured by _fractal asymmetry_ (Drozdz et al., 2015):  
$$\mathcal{A} = \frac{\Delta\alpha_L-\Delta\alpha_R}{\Delta\alpha_L+\Delta\alpha_R}$$
$\Delta\alpha_L=\alpha_0-\alpha_{min}$ and $\Delta\alpha_R=\alpha_{max}-\alpha_{0}$ are the width of the right and the left side of the singularity spectrum curve, respectively and $\alpha_0$, corresponding to $q=0$, usually points to the peak of the $f(\alpha)$ curve. 
For seeing code and examples, look at the ipynb file.


### References
*  Peng, C.-K., S. V. Buldyrev, S. Havlin, M. Simons, H. E. Stanley, and A. L. Goldberger (1994). “Mosaic organization of DNA nucleotides”. In: Physical Review E 49.2, pp. 1685–1689.
*  Kantelhardt, JanW., Stephan A. Zschiegner, Eva Koscielny-Bunde, Shlomo Havlin, Armin Bunde, and H.Eugene Stanley (2002). “Multifractal detrended fluctuation analysis of nonstationary time series”. In: Physica A: Statistical Mechanics and Its Applications 316.1, pp. 87–114.
* Drozdz, Stanislaw and Pawel Swiecimka (2015). “Detecting and interpreting distortions in hierarchical organization of complex time series”. In: Physical Review E 91.3, p. 030902.
* Roeske, Tina C., Damian Kelty-Stephen, and SebastianWallot (2018). “Multifractal analysis reveals music-like dynamic structure in songbird rhythms”. In: Scientific Reports 8.1.