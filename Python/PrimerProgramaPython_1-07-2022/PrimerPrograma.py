string= "0123456789"
subString= ""
start = 2
end = 6
jump = 3


print(f"Cadena principal: {string}")

subString = string[start]
print(f"\nSubcadena con indice en la posición [{start}] es: {subString}")

subString = string[start:end:jump]
print(f"\nSubcadena con indice en la posición [{start}:{end}] con salto de {jump} es: {subString} ")

subString = string[start:end:jump]
print(f"\nSubcadena con indice en la posición [{start}:{end}] con salto de {jump} es: {subString} ")