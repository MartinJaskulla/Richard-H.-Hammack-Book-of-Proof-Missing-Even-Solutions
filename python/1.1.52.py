import numpy as np
from cartesian_plane import draw

def plot(plt, ax):
    # create 100 equally spaced points between -2 and 2
    x = np.linspace(-2, 2, 100)

    # calculate the y value for each element of the x vector
    y = x ** 2
    ax.plot(x, y, color="black")
    ax.plot(x, -y, color="black")

draw(plot)