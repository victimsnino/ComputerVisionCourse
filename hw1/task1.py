import numpy as np

np.set_printoptions(precision=3)
def frobenius_norm(a):
    return np.linalg.norm(a, 'fro')

A = np.matrix([[0.5, 2.16506351, 0.4330127], [-0.8660254, 1.25, 0.25], [0, 0.5, 2.5]])
print(f'Input: \n{A}')

U, S, Vt = np.linalg.svd(A)
print(f'U shape {U.shape} S shape {S.shape} Vt shape {Vt.shape} ')

B = np.matmul(U, Vt)
print(B)

print(f'Frobenius norm: {frobenius_norm(A-B)}')

for i in range(3):
    A_0 = A[:,i]
    B_0 = B[:,i]
    cos_a = np.matmul(A_0.transpose(), B_0) / (np.linalg.norm(A_0) + np.linalg.norm(B_0))
    print(cos_a, np.degrees(np.arccos(cos_a)))