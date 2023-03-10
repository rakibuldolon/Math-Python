import numpy as np
size=int(input('Enter the number of entries in the matrix:')) #size=(number of rows)*(number of columns)
arr=np.array([],dtype=int)
print('Enter the entries of the matrix starting form the 1st element and press enter.')
for i in range(size):
    entry=int(input())
    arr=np.append(arr,entry)
matrix=arr.reshape(int(np.sqrt(size)),int(np.sqrt(size)))
D = np.diag(np.abs(matrix))
S = np.sum(np.abs(matrix), axis=1) - D
if np.all(D >= S):
        print('The matrix is diagonally dominant')
else:
        print('The matrix is not diagonally dominant')
