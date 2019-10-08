import os


def generate_dict(line):
    atributos = ["tipo", "consumo", "energia", "region",
             "comuna", "alteraciones"]
    values = {key: value for key, value in
              zip(atributos, line.strip().split(","))}
    del values["alteraciones"]
    return values

def generator():
    for i in range(4):
        sistema = []
        with open(f"files/sistemas/sistema_{i}.csv", "r", encoding="utf-8") as file:
            sistema.append(generate_dict(file.readline()))
            for line in file:
                sistema.append(generate_dict(line))
        yield sistema

def instanciar_sistema(instalacion, atributos_sistema):
    # No modificar.
    # Se crea la central generadora
    central_generadora = instalacion(**atributos_sistema[0])

    # Se crean y agregan las demás instalaciones
    for atributos in atributos_sistema[1:]:
        nueva_instalacion = instalacion(**atributos)
        central_generadora.agregar_instalacion(nueva_instalacion)
    
    # Se distribuye la energia a través del sistema
    central_generadora.distribuir_energia(central_generadora.energia)

    return central_generadora

