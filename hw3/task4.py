import numpy as np
import math
from task1 import levicivita_matrix
from task2 import invert, rotation_matrix

params = np.matrix([[1,0,0], [0,1,0], [0,0,1]])

rotation = rotation_matrix(45)
# translation in the 'new' system of coordinates, so, first rotate, then move
translation = np.dot(rotation, np.array([[10, 0, 0]]).T)
projection_from_world_to_first = params.dot(np.hstack((rotation, translation)))
projection_from_first_to_world = invert(projection_from_world_to_first)

projection_from_world_to_first = params.dot(np.hstack((rotation_matrix(0), np.array([[0,0,0]]).T)))
F = np.cross(levicivita_matrix(translation), rotation)

# l2 = Fq1
# l1 = q2^T*F

q1 = np.array([[0,0,1]])
q2 = np.dot(projection_from_world_to_first, np.dot(projection_from_first_to_world, q1.T))

l2 = np.dot(F, q1.T)
l1 = np.dot(q2.T, F)

print(l1, l2)