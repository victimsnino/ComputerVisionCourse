import numpy as np
import math

# due to we don't move camera, then we need only find rotation matrix between points...
# Then it is similar to first task, but another matrix

angle = 30
angle_in_rads = angle*math.pi/180
cos = np.cos(angle_in_rads)
sin = np.sin(angle_in_rads)

rotation_matrix_around_x = np.matrix([[1,0,0], [0, cos, -sin], [0, sin, cos]])

print(rotation_matrix_around_x)