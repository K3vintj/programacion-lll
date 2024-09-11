"""
kevin isaac torres jimenez 
222h17061
actividad 3
numeros a letras 
25/08/2024
"""

from num2words import num2words

num = int(input("introduce un numero del 1 al 999: "))

if num >=1000:
    print("el numero no es valido")    
elif num <= 0:
    print("el numero no es valido")
else:
    num_letras= num2words (num, lang="es")
    print(f"***\n{num_letras} pesos 00/100 m.n.\n***")