from cartesian_plane import draw

from matplotlib.patches import Rectangle


def plot(plt, ax):
    ax.add_patch(Rectangle((0, 1), 1, 1, facecolor="lightgray"))


draw(plot, save=False)
