#Calculadora

print("\n")

print("Este programa es una calculadora basica")

operador = input("¿Qué operación desea realizar? Sumar(s), Restar(r), Multiplicar(m), Dividir(d) o Raiz(q)").lower()

if operador == "Raiz" or operador == "r":
    val1 = int(input("Ingresa el valor a sacar la raiz: "))
    print(f"La raiz de {val1} es: {pow(val1, 0.5)}")
else:
    val1 = int(input("Ingresa el primer valor para la operación: "))
    val2 = int(input("Ingresa el segundo valor para la operación: "))

    def calculadora(operador, val1, val2):
        return {
            'sumar': lambda: val1 + val2,
            's': lambda: val1 + val2,
            'restar': lambda: val1 - val2,
            'r': lambda: val1 - val2,
            'multiplicar': lambda: val1 * val2,
            'm': lambda: val1 * val2,
            'dividir': lambda: val1 / val2,
            'd': lambda: val1 / val2
        }.get(operador, lambda: None)
    
    print(f"El resultado de {operador} es: {calculadora(operador, val1, val2)()}")
    




print("\n")