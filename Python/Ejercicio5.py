#Crear una funcion que le enviemos una cantidad y regrese un porsentaje

print("\n")

print("Este programa calcula el precio de despuento de su compra")
a = float(input("Ingresa el total de tu compra: "))
b = float(input("Ingresa el descuento a aplicar en %"))




def Descuento(a , b):
    b /=  100
    descuento = a * b
    precio = a - descuento
    return precio

print(Descuento(a , b))

print("\n")