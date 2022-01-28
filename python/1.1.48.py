from matplotlib.patches import Rectangle
from cartesian_plane import draw

def plot(plt, ax):
    ax.add_patch(Rectangle((1, -4), 3, 8, facecolor="lightgray"))

draw(plot)