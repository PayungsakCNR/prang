import numpy as np

print('#### A ####\n')
##a
def det2x2(A):
    return A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]

A = np.matrix('1 2; 3 4')
print(f'A= {A}, det(A)= {det2x2(A)}')

print('#### B ####\n')
##b
# # (b) Define minor(A,i,j) function
def minor(A, i, j):
    A0_size = len(A)
    B0_size = A0_size - 1
    B = np.zeros((B0_size, B0_size))
    n = i-1 # change to start with 0 index
    m = j-1 # change to start with 0 index
    for r in range(B0_size):
        for c in range(B0_size):
            if (r < n) and (c < m):
                B[r, c] = A[r, c]
            elif (r < n) and (c >= m):
                B[r, c] = A[r, c+1]
            elif (r >= n) and (c < m):
                B[r, c] = A[r+1, c]
            elif (r >= n) and (c >= m):
                B[r, c] = A[r+1, c+1]
    if B0_size == 2:
        return det2x2(B) # This function is already defined
    else:
        return 0
        #return det(B) # This function will be defined later

A = np.matrix('1 2 3; 4 5 6; 7 8 9')
i = 1
j = 2
print(f'A= {A}, minor(A, {i}, {j})= {minor(A, i , j)}')



# # (c) define cofactor(A, i, j) function
print('#### C ####\n')
def cofactor(A, i, j):
    n = i-1 # change index to start with 0
    m = j-1 # change index to start with 0
    return ((-1)**(i+j)) * A[n,m] * minor(A,i,j)


A = np.matrix('1 2 3; 4 5 6; 7 8 9')
i = 1
j = 2
print(f'A= {A}, cofactor(A, {i}, {j})= {cofactor(A,i,j)}')

# # (d) define a function to calculate det(A) of 3x3 matrix
def det3x3(A):
    A0_size = len(A)
    if A0_size == 2:
         return det2x2(A)
    elif A0_size == 3:
         sum_ans = 0
         for n in range(A0_size):
             i = n+1 # change index to start with 1
             sum_ans = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         return XXXXXXXX
    else:
         print('Error')


A = np.matrix('XX XX XX; XX XX XX; XX XX XX')
print(f'A= {XX}, det3x3(A)= {det3x3(A)}')
print('Check the answer with linalg.det():')
print(f'np.linalg.det(A)= {XXXXXXXXXXXXXXX}')
