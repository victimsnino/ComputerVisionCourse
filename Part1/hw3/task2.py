import numpy as np
import math
from task1 import levicivita_matrix

def invert(A):
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    S = np.diag(S)
    return np.dot(np.dot(Vt.transpose(), np.linalg.inv(S)), U.transpose())

if __name__ == '__main__':
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

    # P = K*[R|T]

    # same params
    params = np.matrix([[1,0,0], [0,1,0], [0,0,1]])


    projection_first = params.dot(np.hstack((rotation_matrix_first, translation_first)))
    projection_second = params.dot(np.hstack((rotation_matrix_second, translation_second)))

    center_camera_first = np.array([[0,0,0,1]]).T

    # [e2]=P2*O1
    epipole_2 = np.dot(projection_second, center_camera_first)
    epipole_2 = levicivita_matrix(epipole_2)

    # F = [e2]*P2*(P1)inv
    pseudo_inv = invert(projection_first)
    F = np.dot(np.dot(epipole_2, projection_second), pseudo_inv)
    print(F)

