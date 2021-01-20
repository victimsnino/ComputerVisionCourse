import numpy as np
import math

angle = 45
angle_in_rads = angle*math.pi/180
cos = np.cos(angle_in_rads)
sin = np.sin(angle_in_rads)

rotation_matrix_around_z = np.matrix([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
translation = np.transpose(np.array([[0, 0, 10]]))

fx= 400
fy = fx
cx = 960
cy=540
params = np.matrix([[fx, 0, cx], [0, fy, cy], [0,0,1]])

rotation_and_translation = np.hstack((rotation_matrix_around_z, translation))
result_projection_matrix = np.dot(params, rotation_and_translation)
print(f'Projection matrix:\n{result_projection_matrix}')

point_in_world_coords = np.transpose(np.array([[10, -10, 100]]))
point_in_world_coords = np.vstack((point_in_world_coords, [1]))

point_in_cameras_coords = np.dot(result_projection_matrix, point_in_world_coords)
print(f'Point in camera coords {point_in_cameras_coords}')
print(point_in_cameras_coords.shape)
x, y, z = point_in_cameras_coords
x = float(x/z)
y = float(y/z)
print(f"Point coords in the camera's scope is {x, y}")
