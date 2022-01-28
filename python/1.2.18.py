from cartesian_plane import draw

# Z×Z
def plot(plt, ax):
    for x in range(-3,4):
        for y in range(-3,4):
            plt.scatter(x, y, color="black")
draw(plot)
