def plot_fluctuations(mfdfa_result, ax, title=""):

    scales = mfdfa_result["scales"]
    qs = mfdfa_result["qs"]
    hs = []
    shown_qs = []
    for i, q in enumerate(qs):
        ax.loglog(
            scales,
            mfdfa_result["scaling_function"][:, i],
            "-",
            color="gray",
            markersize=2,
        )
        if q % 1.0 != 0:
            continue
        coef_fitted_line = mfdfa_result["polynomial_coeff"][i]
        hs.append(coef_fitted_line[0])
        shown_qs.append(q)
        lbl = "q={:.0f}".format(q)
        if q == 2:
            ax.loglog(
                scales,
                mfdfa_result["scaling_function"][:, i],
                "s",
                color="black",
                markersize=5,
            )
            ax.loglog(
                scales,
                mfdfa_result["scaling_function"][:, i],
                "--",
                color="black",
                linewidth=4,
                label=lbl,
            )
        else:
            p = ax.loglog(
                scales,
                mfdfa_result["scaling_function"][:, i],
                "o",
                markersize=3,
                label=lbl,
            )

    ax.set_title(title)
    ax.set_xlabel("s")
    ax.set_ylabel("F(s)")


def plot_singularity(mfdfa_result, ax, title=""):

    scales = mfdfa_result["scales"]
    qs = mfdfa_result["qs"]
    hs = []
    shown_qs = []
    for i, q in enumerate(qs):
        if q % 1.0 != 0:
            continue
        coef_fitted_line = mfdfa_result["polynomial_coeff"][i]
        hs.append(coef_fitted_line[0])
        shown_qs.append(q)
        lbl = "q={:.0f}".format(q)
        if q == 2:
            ax.plot(
                mfdfa_result["hq"][i],
                mfdfa_result["Dq"][i],
                "s",
                color="black",
                markersize=5,
            )
            ax.text(
                mfdfa_result["hq"][i],
                mfdfa_result["Dq"][i],
                "q={:.0f}".format(q),
                color="black",
                fontsize=10,
            )
        else:
            if i < mfdfa_result["hq"].size:
                ax.plot(mfdfa_result["hq"][i], mfdfa_result["Dq"][i], "o")

    ax.plot(mfdfa_result["hq"], mfdfa_result["Dq"], "-")
    ax.plot(mfdfa_result["hq"][-1], mfdfa_result["Dq"][-1], "o")

    ax.set_title(title)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"$f(\alpha)$")
