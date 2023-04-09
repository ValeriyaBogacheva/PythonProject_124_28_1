import math
def getL1(x,d1):
    l = math.sqrt((x ** 2) + ((d1*3) ** 2))
    return l

def getL2(h,x,d2):
    l = math.sqrt(((h * 3 - x) ** 2) + (d2 ** 2))
    return l

def getX(d1,theta1):
    radians = math.radians(theta1)
    x = d1 * math.tan(radians) * 3
    return x

def getAllTime(l1,l2,v_sand,n):
    t = (1/(v_sand*5280/60/60)) * (l1 + (n * l2))
    return t
