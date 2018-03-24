'''Lab 3: NumPy'''
'''Name: Bradley Sumoge'''

'''Problem 1'''
def multiply():
    import numpy as np
    A = np.array([ [3,-1,4], [1,5,-9] ])
    B = np.array([ [2,6,-5,3], [5,-8,9,7], [9,-3,-2,-3] ])
    C = (A @ B)
    return C

'''Problem 2'''
def array_ops():
    import numpy as np
    A = np.array([ [3,1,4], [1,5,9], [-5,3,1] ])
    B = (A @ A @ A)
    C = 9*(A @ A)
    D = 15*A
    return -B + C - D

'''Problem 3'''
def np_arrays():
    import numpy as np
    A = np.triu(np.ones((7,7), dtype=np.int))
    I = np.eye(7)
    J = np.triu(np.full_like(I,5))
    B = J - np.tril(np.ones((7,7), dtype=np.int)) - 5*I
    ABA = (A @ B @ A)
    ABA = ABA .astype(np.int64)
    return ABA

'''Problem 4'''
def fancy_index(X):
    import numpy as np
    A = np.array(X)
    mask = A < 0
    A[mask] = 0
    return A

'''Problem 5'''
def stacking():
    import numpy as np
    A = np.array([ [0,2,4], [1,3,5] ])
    B = np.array([ [3,0,0], [3,3,0], [3,3,3] ])
    C = -2*np.eye(3)
    I = np.eye(3)
    zero_1 = np.array([ [0], [0], [0] ])
    zero_2 = np.array([ [0,0,0], [0,0,0] ])
    block_1 = np.hstack((zero_1,A.T,I))
    block_2 = np.hstack((A,zero_2))
    block_3 = np.hstack((B,C))
    matrix = np.vstack((block_1,block_2,block_3))
    return matrix

'''Problem 6'''
def stochastic(X):
    import numpy as np
    A = np.array(X)
    A = A/A.sum(axis=1)[:,None]
    return A