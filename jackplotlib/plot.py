__all__ = ["plot_files"]


import numpy as np
from .subplots import *


def plot_files(infiles, labels, xlabel=None, ylabel=None, separate_axes=False,
               xtick_gran=None, ax=None):
    """
    Parameters
    ----------
    infiles: list
        List of files containing data to be plotted. Each file should contain
        newline-separated floating point numbers.
    labels: list
        List of labels for the data contained in `infiles`. Must be the same
        length as `infiles`.
    separate_axes: bool
        Whether to plot data for these on separate axes.
    xtick_gran: int
        How many spaces between xticks.
    ax: `matplotlib.pyplot.axes.SubplotBase`
        THe axes to plot on.

    Returns
    -------
    Matplotlib figure and axes containing plot.
    """
    assert len(infiles) > 0
    assert len(infiles) == len(labels)
    if separate_axes:
        subplot_dim = [1, len(infiles)]
    else:
        subplot_dim = []

    if ax is None:
        fig, ax = subplots(subplot_dim=subplot_dim)
    else:
        fig = None

    cur_ax = 0
    for fil, label in zip(infiles, labels):
        with open(fil, 'r') as infile:
            lines = infile.readlines()

        data = [float(x) for x in lines]
        x_vals = np.arange(len(data))

        if separate_axes:
            ax_ = ax[0, cur_ax]
            cur_ax += 1
        else:
            ax_ = ax
        ax_.plot(x_vals, data, label=label)
        if xtick_gran:
            ax_.set_xticks(list(range(0, len(data), xtick_gran)))

    return fig, ax
