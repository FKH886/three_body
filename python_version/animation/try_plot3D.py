import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
p = Circle((5, 5), 3)
print(p)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=5, zdir="x")
art3d.pathpatch_2d_to_3d(p, z=5, zdir="z")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
# plt.gca().set_aspect('equal', adjustable='box')
plt.show()
