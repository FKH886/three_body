import random
from itertools import count
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
circle1 = plt.Circle((0, 0), 1, color='r')
ax.add_patch(circle1)
x_track = []
y_track = []
track_length = 300


def animate(i):
    x = np.sin(i/100)
    y = np.cos(i/100)
    x_track.append(x)
    y_track.append(y)
    if len(x_track) > track_length:
        x_track.pop(0)
        y_track.pop(0)
    plt.cla()
    circle1 = plt.Circle((x, y), 1, color='r')
    ax.add_patch(circle1)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    plt.plot(x_track, y_track)
    plt.scatter(x, y, label='Channel 1')
    # plt.plot(x_track, y_track)


plt.gca().set_aspect('equal', adjustable='box')
ani = FuncAnimation(plt.gcf(), animate, interval=10)


plt.show()
