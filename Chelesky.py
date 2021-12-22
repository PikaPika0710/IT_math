import numpy as np

from math import sqrt

from numpy import linalg

check = True

def isPositiveDefiniteMatrix(arr): 
    w, v = linalg.eig(arr) 
    for i in range(0, len(w)):
        if(w[i] < 0): return False
    return True

def cholesky_decomposition(arr):
    global check
    if (isPositiveDefiniteMatrix(arr) == False): 
        print('Error!! Ma tran nay khong phai la ma tran duong\n')
        check = False
        return;
    arr = np.array(arr, float)
    L = np.zeros_like(arr)
    n,_ = np.shape(arr)
    for j in range(n):
        for i in range(j, n):
            if i == j:
                sum = 0
                for k in range(j):
                    sum += L[i, j]**2
                L[i, j] = np.sqrt(arr[i, j] - sum)
            else:
                sum = 0
                for k in range(j):
                    sum += L[i, k]*L[j, k]
                L[i, j] = (arr[i,j] - sum) / L[j, j]
    return L


# main 
#a = [[5, 1.5, 10], [21, 0, 4.5], [10, 2.5, 3]] #Truong hop khong phai ma tran duong
a = [[7.5, 1.5, 0], [1.5, 20, 4.5], [0, 2.5, 3]] 
arr = np.array(a)
print('----Matrix A: ----\n' + str(a) + '\n')
# w: gia tri rieng, v: vecto rieng
w, v = linalg.eig(arr)
print('----Gia tri rieng w: ----\n' + str(w) + '\n') 
print('----Vecto rieng v: ----\n' + str(v) + '\n')
cd = True
L = cholesky_decomposition(arr)
if check == True:
    print('----Matrix L: ----\n' + str(L) + '\n')
    LL = np.dot(L, np.transpose(L))
    print('----Matrix LL: ----\n' + str(LL) + '\n')
