import numpy as np

from cartesian_plane import draw


def plot(plt, ax):
    plt.plot([0, 1], [1, 1], linewidth=2, color="black")


draw(plot)
