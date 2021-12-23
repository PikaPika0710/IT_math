import numpy as np
from math import sqrt
from numpy import linalg

def  cholesky_decomposition(a): 
    a = np.array(a, float)
    L = np.zeros_like(a)
    n,_ = np.shape(a)
    for j in range(n):
        for i in range(j, n):
            if i == j:
                sumk = 0
                for k in range(j-1):
                    sumk += L[i,k]**2
                L[i,j] = np.sqrt(a[i,j] - sumk)
            if i != j:
                sumk = 0
                for k in range(j-1):
                    sumk += L[i,k] * L[j,k]
                L[i,j] = (a[i,j] - sumk) / L[j, j]
    return L

def check_condition_cholesky(a):
    a = np.array(a, float)
    n,m = np.shape(a)
    if n != m: 
        return False
    w, v = linalg.eig(a) 
    for i in range(0, len(w)):
        if w[i] < 0: 
            return False
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i, j] != a[j, i]:
                return False
    return True

if __name__ == '__main__':
    a = np.array([[7.3, 1, 0], [1, 20, 3.5], [0, 3.5, 2]])
    print('----Matrix A: ----\n' + str(a) + '\n')
    if check_condition_cholesky(a):
        v = np.linalg.eigvals(a)
        print('----Matrix V: ----\n' + str(v) + '\n')
        L = cholesky_decomposition(a)
        print('----Matrix L: ----\n' + str(L) + '\n')
        LL = np.dot(L, np.transpose(L))
        print('----Matrix LL: ----\n' + str(LL) + '\n')
    else:
        print('----Matrix A cannot decomposition cholesky ----\n')
    
    