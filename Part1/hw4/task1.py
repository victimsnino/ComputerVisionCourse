import numpy as np
import random

def levicivita_matrix(a):
    x = float(a[0])
    y = float(a[1])
    z = float(a[2])
    return np.matrix([[0, -z, y],
                      [z, 0, -x],
                      [-y, x, 0]])


#F=[e2]*H

e2 = np.array([5, 3, 1])
H = np.matrix([[1,2,3], [4,5,6], [7,8,9]])

F = np.dot(levicivita_matrix(e2), H)
print(F)