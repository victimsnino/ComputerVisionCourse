import numpy as np

np.set_printoptions(precision=3)
def frobenius_norm(a):
    return np.linalg.norm(a, 'fro')

A = np.matrix([[0.5, 2.16506351, 0.4330127], [-0.8660254, 1.25, 0.25], [0, 0.5, 2.5]])

U, S, Vt = np.linalg.svd(A)

B = np.dot(U, Vt)

print(f'Original matrix \n{A}')
print(f'Closest matrix \n{B}')
print(f'Angle is {np.arcsin(B[1,0])*180/np.pi} degrees around OZ line')
