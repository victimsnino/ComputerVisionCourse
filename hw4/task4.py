import numpy as np

def get_fundamental_matrix(first_points, second_points):  
    W = np.zeros((8,9))
    for i in range(8):
        u1, v1 = first_points[i]
        u2, v2 = second_points[i]
        W[i] = [u1*u2, v1*u2, u2, u1*v2, v1*v2, v2, u1, v1, 1]
            
    U,S,Vt = np.linalg.svd(W)
    F = Vt[-1].reshape(3,3)

    U,S,Vt = np.linalg.svd(F)
    S = np.diag(S)
    S[-1,-1] = 0

    F = np.dot(U, np.dot(S,Vt))
    
    return F

angle_in_rads = 0
cos = np.cos(angle_in_rads)
sin = np.sin(angle_in_rads)

rotation_matrix_around_z = np.matrix([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
translation = np.transpose(np.array([[20, 0, 0]]))

params = np.eye(3)
rotation_and_translation = np.hstack((rotation_matrix_around_z, translation))
result_projection_matrix = np.dot(params, rotation_and_translation)

points = [[0,0], [1,1], [2,2], [3,3], [4, 4], [5,5], [6,6], [7,7]]
new_points = []
for point in points:
    point_in_world_coords = np.vstack((np.array([point]).T, [1]))
    point_in_world_coords = np.vstack((point_in_world_coords, [1]))

    new_point = list(np.dot(result_projection_matrix, point_in_world_coords))
    x,y,z = new_point
    new_points.append([float(x/z), float(y/z)])


new_matrix = get_fundamental_matrix(points, new_points)
new_matrix /= new_matrix[-1, -1]
print(new_matrix)