"""
kevin isaac torres jimenez
222h17061
vrs2 de factura 
"""

from datetime import datetime
import random
from convertidor import convertir

class Esperanza:
    @staticmethod
    def generar_folio(longitud=5):
        folio = ''.join(random.choices('0123456789', k=longitud))
        return folio

    @staticmethod
    def fecha():
        fecha = datetime.now().strftime('%d/%m/%y')
        return fecha

    @staticmethod
    def nombre_cliente():
        nombre = input("Introduce el nombre del cliente: ")
        return nombre

    @staticmethod
    def num_telefono():
        numero = input("Introduce el número del cliente: ")
        return numero

    @staticmethod
    def rfc_cliente():
        rfc = input("Introduce el RFC del cliente: ")
        return rfc

    @staticmethod
    def direccion_cliente():
        direccion = input("Introduce la dirección del cliente: ")
        return direccion

class Factura:
    def __init__(self):
        self.empresa = "Esperanza S.A. CV"
        self.folio = Esperanza.generar_folio()
        self.fecha = Esperanza.fecha()
        self.cliente = Esperanza.nombre_cliente()
        self.telefono = Esperanza.num_telefono()
        self.rfc = Esperanza.rfc_cliente()
        self.direccion = Esperanza.direccion_cliente()
        self.productos = []
        self.convertidor = convertir()

    # Métodos get y set
    def get_empresa(self):
        return self.empresa

    def set_empresa(self, value):
        self.empresa = value

    def get_folio(self):
        return self.folio

    def set_folio(self, value):
        self.folio = value

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, value):
        self.fecha = value

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, value):
        self.cliente = value

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, value):
        self.telefono = value

    def get_rfc(self):
        return self.rfc

    def set_rfc(self, value):
        self.rfc = value

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, value):
        self.direccion = value

    def get_productos(self):
        return self.productos

    def agregar_producto(self):
        descripcion = input("Introduce la descripción del producto: ")
        cantidad = float(input("Introduce la cantidad: "))
        precio_unitario = float(input("Introduce el precio unitario: "))
        importe = cantidad * precio_unitario
        self.productos.append((descripcion, cantidad, precio_unitario, importe))

    def calcular_subtotal(self):
        return sum(importe for _, _, _, importe in self.productos)

    def calcular_iva(self, subtotal):
        return round(subtotal * 0.16, 2)

    def calcular_total(self, subtotal, iva):
        return round(subtotal + iva, 2)

    def generar_factura(self):
        subtotal = self.calcular_subtotal()
        iva = self.calcular_iva(subtotal)
        total = self.calcular_total(subtotal, iva)

        # Convertir el total a letras
        total_letras = self.convertidor.convertir_numero_a_letras(int(total))
        centavos = int((total - int(total)) * 100)

        print("\nFactura")
        print(f"Nombre empresa: {self.empresa}")
        print(f"Folio: {self.folio}")
        print(f"Fecha: {self.fecha}")
        print(f"Nombre cliente: {self.cliente}\tTel: {self.telefono}")
        print(f"RFC: {self.rfc}\tDirección: {self.direccion}")
        print("\nProductos:")
        print(f"{'Descripción':<30}{'Cantidad':<10}{'P.Unit':<10}{'Importe':<10}")
        for descripcion, cantidad, precio_unitario, importe in self.productos:
            print(f"{descripcion:<30}{cantidad:<10}{precio_unitario:<10}{importe:<10}")
        print(f"\nSubtotal: {subtotal}")
        print(f"16% IVA: {iva}")
        print(f"Total: {total}")
        print(f"Cantidad en letras: {total_letras} pesos {centavos:02d}/100 m.n.")

# Ejecución del programa
factura = Factura()
num_productos = int(input("¿Cuántos productos deseas agregar? "))
for _ in range(num_productos):
    factura.agregar_producto()

factura.generar_factura()