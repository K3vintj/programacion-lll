"""
kevin isaac torres jimenez 
222h17061
convertir numero decimal a entero 
"""
num_decimal = float(input("Introduce un número: "))
b = num_decimal

if num_decimal > 0:
    while num_decimal > 1.0:
        num_decimal -= 1
    b = b - num_decimal
elif num_decimal < 0:
    while num_decimal < -1.0:
        num_decimal += 1
    b = b - num_decimal
else:
    b = 0
print(f"El valor entero es: {b:.0f}")