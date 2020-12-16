import math
import numpy as np
from pyquaternion import Quaternion

angle_in_rads = 45*math.pi/180
cos = np.cos(angle_in_rads)
sin = np.sin(angle_in_rads)

rotation_matrix_first = np.matrix([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
translation_first = np.array([[0,0,0]]).T

angle_in_rads = -45*math.pi/180
cos = np.cos(angle_in_rads)
sin = np.sin(angle_in_rads)

rotation_matrix_second = np.matrix([[cos, 0, sin], [0, 1, 0], [-sin, 0, cos]])
translation_second =np.array([[10, 0, 0]]).T

rotation_quart_first = Quaternion(matrix=rotation_matrix_first)
rotation_quart_second = Quaternion(matrix=rotation_matrix_second)

params = np.matrix([[1,0,0], [0,1,0], [0,0,1]])

def get_position(percent):
    rotation_quart = rotation_quart_first*(1-percent) + rotation_quart_second*(percent)
    rotation = rotation_quart.rotation_matrix
    translation = translation_first*(1-percent) + translation_second*(percent)
    return params.dot(np.hstack((rotation, translation)))

print(f'get_position(0) == first_projection  : {np.allclose(params.dot(np.hstack((rotation_matrix_first, translation_first))), get_position(0))}')
print(f'get_position(1) == second_projection : {np.allclose(params.dot(np.hstack((rotation_matrix_second, translation_second))),get_position(1))}')
print(get_position(0.5))