import numpy as np
import math

# Imagine, that first camera located in the world's (0,0,0) with zero rotation. Then
# F = [T]*R

def levicivita_matrix(a):
    x = float(a[0])
    y = float(a[1])
    z = float(a[2])
    return np.matrix([[0, -z, y],
                      [z, 0, -x],
                      [-y, x, 0]])

if __name__ == "__main__":
    angle = 45
    angle_in_rads = angle*math.pi/180
    cos = np.cos(angle_in_rads)
    sin = np.sin(angle_in_rads)

    rotation_matrix_around_z = np.matrix([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    # translation in the 'new' system of coordinates, so, first rotate, then move
    translation = np.dot(rotation_matrix_around_z, np.array([[10, 0, 0]]).T)

    F = np.cross(levicivita_matrix(translation), rotation_matrix_around_z)
    print(F)
