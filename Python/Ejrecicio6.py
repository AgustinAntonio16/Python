#ingresar 2 digitos y decir cual es par o si ambos lo son

print("\n")
print("Este programa solicitará 2 números y te dirá cual de esllos es par o si ambos lo son")

a = float(input("Ingresa el primer número"))
b = float(input("ingresa el segundo número"))

if (a % 2) == 0 and (b % 2) == 0:
    print(f"Ambos son par")
elif (a % 2) == 0 and (b % 2) == 1:
    print(f"El númer {a} es PAR")
elif (a % 2) == 1 and (b % 2) == 0:
    print(f"El númer {b} es PAR")
elif (a % 2) == 1 and (b % 2) == 1:
    print(f"ninguno es PAR")


print("\n")