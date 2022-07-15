import math 

print("\n")

area = 0
perimetro = 0

def Hallo(r):
    area = math.pi * (r**2)
    perimetro = math.pi * (r*2)
    return area,perimetro


print(Hallo(5))

print("\n")