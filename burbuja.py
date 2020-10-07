def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def burbuja_optimizado(A):
    n = len(A)
    swapcounter = 0
    for i in range(1, n):
    	if i==n and swapcounter==0:
    		return A
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapcounter +=1
