from datetime import datetime

# Datos de la factura
empresa = "Tornillos S.A. CV"
factura_num = 123
fecha = datetime(2024, 9, 3).strftime('%d/%m/%y')
cliente = "XYZ"
telefono = "9933"

# Lista de productos (item, descripcion, cantidad, precio unitario)
productos = [
    (1, "Tuerca 3/4''", 10, 2.5),
    (2, "Tornillos rosca 1/2''", 5, 15),
    (3, "Arandela estandar", 20, 2)
]

# Calcular subtotales
subtotal = sum(cantidad * precio for _, _, cantidad, precio in productos)
iva = round(subtotal * 0.16, 2)
total = round(subtotal + iva, 2)

# Convertir total a texto (simplificado)
def convertir_a_letras(numero):
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = {11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince"}
    letras = []

    entero = int(numero)
    centavos = int((numero - entero) * 100)

    if entero == 100:
        letras.append("cien")
    elif entero > 9 and entero < 16:
        letras.append(especiales[entero])
    elif entero >= 10 and entero < 100:
        decena = entero // 10
        unidad = entero % 10
        if decena > 0:
            letras.append(decenas[decena])
        if unidad > 0:
            if decena == 2:
                letras[-1] = letras[-1][:-1] + "i" + unidades[unidad]  # "veintiuno", "veintidós", etc.
            else:
                letras.append(unidades[unidad])
    elif entero < 10:
        letras.append(unidades[entero])
    else:
        letras.append("Número fuera de rango")

    letras.append(f"{centavos}/100 m.n.")
    
    return " y ".join(letras).capitalize()

total_letras = convertir_a_letras(total)

# Generar la factura
print("Factura")
print(f"Nombre empresa: {empresa}")
print(f"Fecha: {fecha}\t\tFactura No: {factura_num}")
print(f"Nombre cliente: {cliente}\t\tTel: {telefono}")
print()
print(f"{'Item':<10}{'Descripción':<30}{'Cantidad':<10}{'P.Unit':<10}{'Importe':<10}")
for item, desc, cantidad, precio in productos:
    importe = cantidad * precio
    print(f"{item:<10}{desc:<30}{cantidad:<10}{precio:<10}{importe:<10}")
print()
print(f"Subtotal: {subtotal}")
print(f"16% IVA: {iva}")
print(f"Total: {total}")
print()
print(f"Cantidad en letras: {total_letras}")

