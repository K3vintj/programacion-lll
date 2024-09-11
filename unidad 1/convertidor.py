class convertir():
    def convertir_numero_a_letras(self, numero):
        unidades = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        dec_especiales = ["", "", "veinti"]
        especiales = ["once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
        centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

        entero = int(numero)
        
        if entero == 100:
            return "cien"
        
        elif entero < 10:
            return unidades[entero]
        
        elif entero < 20:
            return especiales[entero - 11]

        elif entero < 100:
            if entero % 10 == 0:
                return decenas[entero // 10]
            elif entero // 10 == 2:
                return dec_especiales[entero // 10] + unidades[entero % 10]
            else:
                return decenas[entero // 10] + " y " + unidades[entero % 10]
        
        elif entero < 1000:
            if entero % 100 == 0:
                return centenas[entero // 100]
            else:
                return centenas[entero // 100] + " " + self.convertir_numero_a_letras(entero % 100)
        
        else:
            miles = entero // 1000
            resto = entero % 1000
            miles_texto = ""
            if miles == 1:
                miles_texto = "mil"
            else:
                miles_texto = self.convertir_numero_a_letras(miles) + " mil"
            
            if resto == 0:
                return miles_texto
            else:
                return miles_texto + " " + self.convertir_numero_a_letras(resto)

    def solicitar_valor(self):
        while True:
            entrada = input("Introducir un valor a convertir (terminar con x): ")
            
            if entrada.lower() == "x":
                break
            
            try:
                numero = float(entrada)
                if numero < 1 or numero > 99999:
                    print("El número está fuera del rango permitido (1 - 99,999).")
                    continue
                
                parte_entera = int(numero)
                parte_decimal = round((numero - parte_entera) * 100)
                
                letras = self.convertir_numero_a_letras(parte_entera)
                print(f"Salida: {letras} pesos {parte_decimal:02d}/100 m.n.")
            
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

# Para ejecutar
#conv = convertir()
#conv.solicitar_valor()
