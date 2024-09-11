"""
kevin isaac torres jimenez 
222h17061
numeros a letras mejorado
"""

def convertir_numero_a_letras(numero):
    unidades = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    dec_especiales = ["", "", "veinti"]
    especiales = ["once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if numero == 100:
        return "cien"
    
    elif numero < 10:
        return unidades[numero]
    
    elif numero < 20:
        return especiales[numero - 11]

    elif numero < 100:
        if numero % 10 == 0:
            return decenas[numero // 10]
        elif numero // 10 == 2:
            return dec_especiales[numero//10]+unidades[numero % 10]
        else:
            return decenas[numero // 10] + " y " + unidades[numero % 10]
    elif numero < 1000:
        if numero % 100 == 0:
            return centenas[numero // 100]
        else:
            return centenas[numero // 100] + " " + convertir_numero_a_letras(numero % 100)
    else:
        miles = numero // 1000
        resto = numero % 1000
        miles_texto = ""
        if miles == 1:
            miles_texto = "mil"
        else:
            miles_texto = convertir_numero_a_letras(miles) + " mil"
        
        if resto == 0:
            return miles_texto
        else:
            return miles_texto + " " + convertir_numero_a_letras(resto)

def solicitar_valor():
    while True:
        entrada = input("Introducir un valor a convertir: ")
        if entrada.isdigit() and 1 <= int(entrada) <= 99999:
            numero = int(entrada)
            letras = convertir_numero_a_letras(numero)
            print(f"Salida: {letras} pesos 00/100 m.n.")
        else:
            print("adiós!")
            break

solicitar_valor()