from cartesian_plane import draw

def plot(plt, ax):
    circle = plt.Circle((0, 0), 1, color="lightgray")
    ax.add_patch(circle)


draw(plot, save=False)
