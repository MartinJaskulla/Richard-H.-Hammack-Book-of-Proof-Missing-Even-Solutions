from cartesian_product import cartesian_product
from cartesian_plane import draw

A = [-1, 0, 1]
B = [1, 2, 3]

points = cartesian_product([A,B])

def plot(plt, ax):
    for point in points:
        plt.scatter(point[0], point[1], color="black")

draw(plot)
