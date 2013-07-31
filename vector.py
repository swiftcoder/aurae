
import math

def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def vadds(a, b):
    return (a[0]+b, a[1]+b, a[2]+b)

def vsub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def vmuls(a, b):
    return (a[0]*b, a[1]*b, a[2]*b)

def vdivs(a, b):
    return (a[0]/b, a[1]/b, a[2]/b)

def vlen(a):
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)

def vnorm(a):
    l = vlen(a)
    return a if l == 0 else vmuls(a, 1.0/l)
