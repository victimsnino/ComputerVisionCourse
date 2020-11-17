import numpy as np
from numpy.core.fromnumeric import searchsorted

points_first  = [[0,0], [150, 0], [150, 150],[0,150]]
points_second = [[100, 100], [200, 80], [220, 80], [100, 200]]
A = []
for point1, point2 in zip(points_first, points_second):
    x1, y1 = point1
    x2, y2 = point2
    A.append([-x1, -y1, -1,    0,   0,  0, x2*x1, x2*y1, x2])
    A.append([0,     0,   0, -x1, -y1, -1, y2*x1, y2*y1, y2])

A= np.matrix(A)

U, S, Vt = np.linalg.svd(A)
H_as_vectr = Vt[-1, :]
H_matrix = H_as_vectr.reshape((3,3))
print(H_matrix)

#Check....

points_as_matrix = np.matrix(points_first)
ones_vector = np.array([[1]*len(points_first)]).T
points_as_matrix = np.hstack((points_as_matrix, ones_vector))

for i in range(points_as_matrix.shape[0]):
    transformed_point = np.dot(H_matrix, points_as_matrix[i, :].T)
    x,y,z = transformed_point
    x = float(np.round(x/z))
    y = float(np.round(y/z))
    print([x,y], points_second[i])

