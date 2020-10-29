import numpy as np

def generate_matrix(n):
    res = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            res[i,j] = np.divide(1, ((i+1)+(j+1)-1))
    return res

for n in [3, 10]:
    print('=============================================================')
    A = generate_matrix(n)

    U, S, Vt = np.linalg.svd(A, full_matrices=True)
    S = np.diag(S)

    A_invert = np.matmul(np.matmul(Vt.transpose(), np.linalg.inv(S)), U.transpose())
    print(f"Original matrix \n{A} \nInvert matrix \n{A_invert}")

    A_invert_np = np.linalg.inv(A)
    print(f'Is eqaul to np invert: {np.allclose(A_invert, A_invert_np, rtol=0.001)}')