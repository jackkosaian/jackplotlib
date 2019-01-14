__all__ = ["cdf"]

def cdf(ax, data, color=None, label=None, linestyle='solid', linewidth=1.5):
    sorted_data = np.sort(data)
    yvals = np.arange(len(sorted_data)) / float(len(sorted_data)-1)
    return ax.plot(sorted_data, yvals, color=color, label=label,
                   linestyle=linestyle, linewidth=linewidth)
