from cartesian_plane import plane
from matplotlib.patches import Rectangle

(plt, ax) = plane()

ax.add_patch(Rectangle((0, 1), 1, 1, facecolor="lightgray"))

plt.show()