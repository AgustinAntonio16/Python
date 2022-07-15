
print("\n")

print("Este ejercicio mostrará si un número ingresado pertenese o no a la serie de fibonacci")
n = 0
n1 = 1
n2 = 0

num = int(input("Ingrese el número a verificar: "))

while n2 < num:
    n2 = n + n1
    print(n2)
    n = n1
    n1 = n2

if n2 == num:
    print("pertenese")
else:
    print("no pertenese") 

print("\n")