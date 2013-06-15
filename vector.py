
import math

def vadd(a, b):
    return tuple(a[i] + b[i] for i in range(3))

def vadds(a, b):
    return tuple(a[i] + b for i in range(3))

def vsub(a, b):
    return tuple(a[i] - b[i] for i in range(3))

def vmuls(a, b):
    return tuple(a[i] * b for i in range(3))

def vdivs(a, b):
    return tuple(a[i] / b for i in range(3))

def vlen(a):
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)

def vnorm(a):
    l = vlen(a)
    return a if l == 0 else vmuls(a, 1.0/l)
