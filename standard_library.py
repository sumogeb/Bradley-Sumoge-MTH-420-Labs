'''Lab 2: The Standard Library'''
'''Name: Bradley Sumoge'''

'''Problem 1'''
def MMA(L):
    print(min(L),max(L),sum(L)/len(L))
    return

'''Problem 2'''
'''int is immutable'''
'''str is immutable'''
'''list is mutable'''
'''tuple is immutable'''
'''set is immutable'''

'''Problem 3'''
def hypotenuse(x,y):
    import calculator
    import math
    a = calculator.calculator_product(x,x)
    b = calculator.calculator_product(y,y)
    c = calculator.calculator_sum(a,b)  
    d = math.sqrt(c)
    return d

'''Problem 4'''
def power(A):
    from itertools import chain,combinations
    z = list(A)
    return chain.from_iterable(combinations(z,r) for r in range(len(z)+1))

def power_set(l):
    return list(power(l))