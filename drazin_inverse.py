'''Lab 6: Effective Resistance'''
'''Name: Bradley Sumoge'''

'''Problem 1'''
def drazin_check(A,AD,k):
    import numpy as np  
    A = np.array(A)
    AD = np.array(AD)
    if np.all(A @ AD) == np.all(AD @ A):
        if np.all(A**(k+1) @ AD) == np.all(A**k):
            if (np.all(AD @ A @ AD) == np.all(AD)):
                return True        
    else:
        return False
    
'''Problem 2'''
def drazin_compute(A):
    from scipy import linalg as la
    import numpy as np
    A = np.array(A)
    T,Z = la.schur(A)
    f = lambda x: abs(x) > 0
    T1,Z1,k = la.schur(A, sort=f)
    return T1