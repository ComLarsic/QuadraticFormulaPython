import math

def abc(a,b,c):
    d = ((b**2) -4*a*c)
    xPos = (-b + math.sqrt(d))/(2*a)
    xNeg = (-b - math.sqrt(d))/(2*a)

    return f"{xPos} v {xNeg}, D = {d}"

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

try:
    print(abc(a, b, c))
except:
    print("given arguments are invalid, D < 0")