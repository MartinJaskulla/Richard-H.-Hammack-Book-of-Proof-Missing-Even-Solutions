import numpy as np
from cartesian_plane import draw


def plot(plt, ax):
    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(-4, 4, 100)

    # calculate the y value for each element of the x vector
    sqaured = (x ** 2)

    natural_numbers_to_1000 = range(1, 1000)
    for n in natural_numbers_to_1000:
        y = sqaured / n
        ax.plot(x, y, color="black")


draw(plot)
