from leer_archivos import read_file


class Ayudante:
    def __init__(self, nombre, rango, tipo, afinidad, eficiencia):
        # Rellenar
        pass

    def agregar_ayudante(self, ayudante):
        # Rellenar
        pass


def grupo_mayor_eficiencia(sistema):
    # Rellenar
    pass


def imprimir_grupo(grupo, visitados):
        # Rellenar
    pass


def instanciar_cuerpo_ayudantes(ayudantes):
    # No modificar
    enzini = Ayudante(**ayudantes[0])
    for data in ayudantes[1:]:
        enzini.agregar_ayudante(Ayudante(**data))
    return enzini


if __name__ == "__main__":
    # No modificar
    ayudantes = read_file()
    cuerpo_ayudantes = instanciar_cuerpo_ayudantes(ayudantes)
    grupo_mayor_eficiencia(cuerpo_ayudantes)
