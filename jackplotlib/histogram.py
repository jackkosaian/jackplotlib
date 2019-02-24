__all__ = ["histogram"]


import numpy as np


def histogram(ax, data, num_bins=100, color=None, label=None):
    bins = np.linspace(min(data), max(data), num_bins)
    hist = np.histogram(data, bins=bins)
    return ax.bar(bins[:-1], hist[0], width=bins[1]-bins[0], color=color, label=label)
