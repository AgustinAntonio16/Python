#DE UN CIRCULO CALCULAR RADIO Y CIRCUNFERENCIA
import math
print("\n")

print("En este ejercicio calcularemos el are y circunferencia de un circulo")

r = int(input("ingresa el valor del radio: "))

area = (math.pi) * (r**2)
longitud = 2 * (math.pi) * r

print(f"El area del circulo es: {area:.2f} y su circunferencia es: {longitud:.3f}")

print("\n")
