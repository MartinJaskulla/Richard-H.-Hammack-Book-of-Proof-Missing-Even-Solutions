import numpy as np

from cartesian_plane import draw

# [1,2] * {1,1.5,2}

def plot(plt, ax):
    plt.plot([1, 2], [1, 1], linewidth=2, color="black")
    plt.plot([1, 2], [1.5, 1.5], linewidth=2, color="black")
    plt.plot([1, 2], [2, 2], linewidth=2, color="black")


draw(plot)
