import numpy as np

np.set_printoptions(precision=5)

def generate_matrix(n):
    res = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            res[i,j] = (i+1)+(j+1)-1
    return res

n = 4
A = generate_matrix(n)
print(f'Initial matrix = {A}')

U, S, Vt = np.linalg.svd(A)
for i in range(n):
    if np.isclose(S[i], 0) ==False:
        continue
    x =Vt[i,:]
    B = A*x
    print(f'Solution for A*x = 0: \n x: {x}\n AX:\n{B} \n B=\n {np.sum(B, axis=1)}')
    print()


print(0.3925*2 -0.80808*3 + 4*0.43866 -0.02308*5)