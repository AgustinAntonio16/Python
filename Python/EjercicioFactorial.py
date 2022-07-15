import math 
print("\n")

print("Este ejercicio realizará a partir de un número 'n' la siguiente suma")
print("1/1! - 2/2! + 3/3! - 4/4!... n/n!")

n = int(input("Ingrese el valor de n: "))
resultado = 0

for i in range(1 , n+1):
    if (i % 2) == 1:
        resultado += (i/math.factorial(i))
        print(f"i = {i}", resultado)
    elif (i % 2) == 0:
        resultado -= (i/math.factorial(i))
        print(f"i = {i}", resultado)

print("\n")