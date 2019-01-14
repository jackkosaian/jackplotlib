__all__ = ["subplots"]

import matplotlib.pyplot as plt


def subplots(font_size=12, width_height=None, family='Times New Roman', subplot_dim=[]):
    plt.rc('font', family=family, size=font_size, weight='light')
    fig, ax = plt.subplots(*subplot_dim)

    # Handle the case where we only have one plot
    if len(subplot_dim) == 0:
        ax = [ax]
    else:
        ax = ax.flatten()

    for ax_ in ax:
        ax_.spines['right'].set_visible(False)
        ax_.spines['top'].set_visible(False)

        if width_height:
            w = width_height[0]
            h = width_height[1]
            l = ax_.figure.subplotpars.left
            r = ax_.figure.subplotpars.right
            t = ax_.figure.subplotpars.top
            b = ax_.figure.subplotpars.bottom
            figw = float(w)/(r-l)
            figh = float(h)/(t-b)
            ax_.figure.set_size_inches(figw, figh)

    # When we only have one plot, don't return an array.
    if len(ax) == 1:
        ax = ax[0]

    return fig, ax

