from leer_archivos import obtener_sistema

"""
obtener_sistema:        Funcion que al ser llamada retorna una lista donde el
                        elemento 0 es el generador del sistema y los demas son
                        el resto de las instalaciones.
                        Cada instalacion es un dict.

ALTERACIONES:           Dict de la forma; alteracion: valor
"""


class Instalacion:
    """
    Contiene toda la información de cada instalacion más un diccionario
    auxiliar.
    """
    hijos = {
        "Generadora": "Distribuidora Regional",
        "Distribuidora Regional": "Distribuidora Comunal",
        "Distribuidora Comunal": "Casa",
        "Casa": None
    }

    def __init__(self, **kwargs):
        self.tipo = kwargs["tipo"]
        self.region = kwargs["region"]
        self.comuna = kwargs["comuna"]
        self.hijos = []
        self.consumo = float(kwargs["consumo"])
        self.energia = float(kwargs["energia"])

    def agregar_instalacion(self, instalacion):
        """
        Agrega la instalación al sistema.
        """
        if instalacion.tipo == Instalacion.hijos[self.tipo]:
            """
            Si la instalacion a agregar es del tipo de nuestros hijos
            la agregamos
            """
            self.hijos.append(instalacion)
        else:
            if instalacion.tipo == "Distribuidora Comunal":
                """
                Si no es nuestro hijo y es comunal, buscamos la Regional
                adecuada para agregar.
                """
                self.get_region(instalacion).agregar_instalacion(instalacion)
            elif instalacion.tipo == "Casa":
                """
                Si no es nuestro hijo y es Casa buscamos la Regional y
                Comunal adecuada para agregar.
                """
                self.get_region(instalacion).get_comuna(
                    instalacion).agregar_instalacion(instalacion)

    def distribuir_energia(self, energia):
        """
        Distribuimos nuestra energía a nuestros hijos
        """
        cantidad_hijos = len(self.hijos)
        self.energia = energia
        for hijo in self.hijos:
            energia_hijo = (self.energia - self.consumo) / cantidad_hijos
            energia_hijo = max(0, energia_hijo)
            hijo.distribuir_energia(energia_hijo)

    def contar_instalaciones(self):
        """
        Retornamos 1 y sumamos uno por cada uno de nuestros hijos
        """
        return 1 + sum(hijo.contar_instalaciones() for hijo in self.hijos)

    def contar_consumo(self):
        """
        Returnamos nuestro consumo más la suma del consumo de nuestros hijos
        """
        return self.consumo + sum(hijo.contar_consumo() for hijo in self.hijos)

    def get_region(self, instalacion):
        """
        Funcion auxiliar que nos retorna un match de region en nuestros hijos
        """
        return next(filter(lambda item: item.region == instalacion.region,
                           self.hijos))

    def get_comuna(self, instalacion):
        """
        Funcion auxiliar que nos retorna un match de comuna en nuestros hijos
        """
        return next(filter(lambda item: item.comuna == instalacion.comuna,
                           self.hijos))

    def __repr__(self):
        return f"{self.tipo}: {self.region}, {self.comuna}"


def instanciar_sistema(atributos_sistema):
    # No modificar.
    # Se crea la central generadora
    central_generadora = Instalacion(**atributos_sistema[0])

    # Se crean y agregan las demás instalaciones
    for atributos in atributos_sistema[1:]:
        nueva_instalacion = Instalacion(**atributos)
        central_generadora.agregar_instalacion(nueva_instalacion)
    
    # Se distribuye la energia a través del sistema
    central_generadora.distribuir_energia(central_generadora.energia)

    return central_generadora


def resumen_sistema(sistema):
    print("Resumen del Sistema:")
    print(sistema)
    print(f"Consumo Total: {sistema.contar_consumo()}")
    print(f"Número de Instalaciones: {sistema.contar_instalaciones()}")


def comuna_mayor_gasto(sistema):
    print(max((comuna for region in sistema.hijos for comuna in region.hijos),
              key=lambda comuna: comuna.contar_consumo()))


def casas_insuficiencia(sistema):
    print("Casas con Insuficiencia:", end=" ")
    print(len(list(filter(lambda casa: casa.energia < casa.consumo,
                          (casa for region in sistema.hijos
                           for comuna in region.hijos
                           for casa in comuna.hijos)))))


if __name__ == '__main__':
    # No modificar
    # Se probará DCCableling para 4 sistemas electricos:
    for i in range(1, 5):
        print(f"CONSULTAS SISTEMA ELÉCTRICO N°{i}")
        print("---------------------" * 2)
        atributos_de_sistema = obtener_sistema()
        sistema_electrico = instanciar_sistema(atributos_de_sistema)
        resumen_sistema(sistema_electrico)
        comuna_mayor_gasto(sistema_electrico)
        casas_insuficiencia(sistema_electrico)
        print("---------------------" * 2)
