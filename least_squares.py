'''Lab 5: Least Squares'''
'''Name: Bradley Sumoge'''

'''Problem 1'''
def QR(A,b):
    import pprint
    import scipy
    import scipy.linalg

    Q, R = scipy.linalg.qr(A)

    print("A:")
    pprint.pprint(A)

    print("Q:")
    pprint.pprint(Q)

    print("R:")
    pprint.pprint(R)
    Qb = (Q.T @ b)
    x = scipy.linalg.solve(R,Qb)
    print("X:")
    pprint.pprint(x)
    return

'''Problem 2'''
def housing():
    import numpy as np

    y0 = np.array([0, 1])
    y1 = np.array([1, 1])
    y2 = np.array([2, 1])
    y3 = np.array([3, 1])
    y4 = np.array([4, 1])
    y5 = np.array([5, 1])
    y6 = np.array([6, 1])
    y7 = np.array([7, 1])
    y8 = np.array([8, 1])
    y9 = np.array([9, 1])
    y10 = np.array([10, 1])
    
    A = np.vstack((y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10))
    B = np.array([169.575,176.350,180.258,184.800,189.542,195.717,203.158,
                  209.583,216.255,217.058,216.254])
    
    QR(A,B)
    return QR(A,B)

'''Problem 3'''
def poly(A,b):
    from scipy import linalg as la
    import numpy as np
    x1 = la.lstsq(A, b)[0]
    x2 = np.polyfit(A,b)[0]
    return x1,x2