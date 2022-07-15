print("\n")

a = float(input("Ingresa el número 1"))
b = float(input("Ingresa el número 2"))
c = float(input("Ingresa el número 3"))

if a > b and a > c:
    print(f"{a} es el mayor")
elif b > a and b > c:
    print(f"{b} es el mayor")
else:
    print(f"{c} es el mayor")
print("\n")