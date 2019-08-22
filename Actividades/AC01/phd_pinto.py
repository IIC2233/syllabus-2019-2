import os
'''
Debes completar las properties de la clase DrPintoDesencriptador
'''


class DrPintoDesencriptador:
    def __init__(self):
        self._ruta = None

    @property
    def ruta(self):
        # completar
        pass

    @ruta.setter
    def ruta(self, nueva_ruta):
        # completar
        pass

    @property
    def texto_desencriptado(self):
        # completar
        pass

    # Metodos usados para desencriptar, no tocar
    def recuperar_cadena_de_numeros(self, mensaje_encriptado):
        cadena_de_inicio = self.recuperar_cadena_de_inicio(mensaje_encriptado)
        return self.aplicar_cambio_de_orden(cadena_de_inicio)

    @staticmethod
    def recuperar_cadena_de_inicio(mensaje_encriptado):
        cadena_inicio = "2233" + mensaje_encriptado[0:10]
        c = 0
        while len(cadena_inicio) != 256:
            if c == 0:
                cadena_inicio += "2233"
                c = 1
            else:
                cadena_inicio += mensaje_encriptado[0:10]
                c = 0
        return cadena_inicio

    @staticmethod
    def aplicar_cambio_de_orden(cadena):
        cadena_numeros = list(range(0, 256))
        cadena_inicio = list(cadena)
        c = 0
        while c <= 255:
            indice_a_cambiar = c + int(cadena_inicio[c])
            if indice_a_cambiar > 255:
                indice_a_cambiar -= 256
            aux = str(cadena_numeros[c])
            cadena_numeros[c] = str(cadena_numeros[indice_a_cambiar])
            cadena_numeros[indice_a_cambiar] = aux
            c += 1
        final = []
        for i in cadena_numeros:
            num_bin = bin(int(i)).replace("b", "")
            while len(num_bin) < 8:
                num_bin = "0" + num_bin
            if len(num_bin) > 8:
                num_bin = num_bin[1:]
            final.append(num_bin)
        return "".join(final)

    @staticmethod
    def recuperar_cadena_asunto(mensaje_encriptado, cadena):
        cadena_asunto = ""
        c = 0
        for i in mensaje_encriptado[10:]:
            if i == "1":
                if cadena[c] == "0":
                    cadena_asunto += "1"
                else:
                    cadena_asunto += "0"
            else:
                cadena_asunto += cadena[c]
            c += 1
        return cadena_asunto

    @staticmethod
    def quitar_cifrado_cesar(asunto_mensaje):
        letras = []
        c = 8
        while c <= len(asunto_mensaje):
            caracter = asunto_mensaje[c - 8:c]
            letras.append(caracter)
            c += 8
        asunto = ""
        for i in letras:
            formato_ascii = int(i, 2) - 10
            asunto += chr(formato_ascii)
        return asunto

    def desencriptar(self):
        desencriptado = []
        with open(self.ruta, 'r', encoding='utf8') as archivo:
            for linea in archivo:
                cadena = self.recuperar_cadena_de_numeros(linea.strip())
                cadena_asunto = self.recuperar_cadena_asunto(linea.strip(), cadena)
                desencriptado.append(self.quitar_cifrado_cesar(cadena_asunto))
        print('Texto desencriptado')
        return desencriptado
