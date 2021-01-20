import numpy as np
import math
from task1 import levicivita_matrix
from task2 import rotation_matrix

params = np.matrix([[1,0,0], [0,1,0], [0,0,1]])

angle = 45
angle_in_rads = angle*math.pi/180
cos = np.cos(angle_in_rads)
sin = np.sin(angle_in_rads)

rotation = np.matrix([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
translation = np.array([[10, 0, 0]]).T
projection_first = params.dot(np.hstack((rotation, translation)))

rotation_second = np.eye(3)
translation_second = np.array([[0,0,0]])
projection_second = params.dot(np.hstack((rotation_second, translation_second.T)))

# e2=P2*O1
# in one case P2 
epipole_2 = np.dot(projection_second, np.vstack((translation, [1])))

epipole_1 = np.dot(projection_first,  np.vstack((translation_second.T, [1])))

print(epipole_2, epipole_1)