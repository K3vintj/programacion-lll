"""
kevin isaac torres jimenez 
222h17061
actividad 1 
calcular numeros primos en un rango dado
18/08/2024
"""
# Solicitar al usuario que ingrese el rango
inicio_rango = int(input("Introduce el inicio del rango: "))
fin_rango = int(input("Introduce el fin del rango: "))

# Recorrer el rango de números
for num in range(inicio_rango, fin_rango + 1):
    if num <= 0:
        continue  # Saltar los números menores o iguales a 0
    
    es_primo = True
    factores = ""
    
    # Comprobar si el número es primo
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            factores += f"{i}, "
            if i != num // i:
                factores += f"{num // i}, "
    
    # Imprimir el número y su estado
    if es_primo:
        print(f"{num} es un número primo.")
    else:
        factores = factores.rstrip(", ")  # Eliminar la última coma
        print(f"{num} no es un número primo. Factores: {factores}")
