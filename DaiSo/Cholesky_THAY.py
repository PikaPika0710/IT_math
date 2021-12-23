

import numpy as np

from math import sqrt

def cholesky_decomposition(a):

    a = np.array(a,float)

    L = np.zeros_like(a)

    n,_ = np.shape(a)

    for j in range(n):

        for i in range(j,n):

            if i == j:

                sumk = 0

                for k in range(j):

                    sumk += L[i,j]**2

                L[i,j] = np.sqrt(a[i,j]-sumk)

            else:

                sumk = 0

                for k in range(j):

                    sumk+=L[i,k]*L[j,k]

                L[i,j] = (a[i,j]-sumk)/L[j,j]

    return L

if __name__ == '__main__':

    a= np.array([[7.3, 1, 0], [1, 20, 3.5], [0, 3.5, 2]])

print('----- Matrix A: -----\n' + str(a) + '\n')

# ====> Lưu ý

v= np.linalg.eigvals(a)

print('----- Matrix V: -----\n' + str(v) + '\n')

L = cholesky_decomposition(a)

print('----- Matrix L: -----\n' + str(L) + '\n')

LL = np.dot(L, np.transpose(L))

print('----- Matrix LL: -----\n' + str(LL) + '\n')





