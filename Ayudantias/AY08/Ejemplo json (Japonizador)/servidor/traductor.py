import json

ch = "#"
ny = "*"

# se carga el diccionario
with open("diccionario.json", 'r', encoding="utf-8") as file:
    diccionario = json.loads(file.read())

def reemplazar_tildes(palabra):
    nueva_palabra = ""
    diccionario_letras = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                          'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'}
    for letra in palabra:
        if letra in "áéíóúÁÉÍÓÚ":
            nueva_palabra += diccionario_letras[letra]
        else:
            nueva_palabra += letra
    return nueva_palabra

def manejar_q(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra2 = palabra[indice_letra]
        if letra2 == "u":
            indice_letra += 1
            if indice_letra < len(palabra):
                letra3 = palabra[indice_letra]
                if letra3 in "ei":
                    letras_por_agregar = "k" + letra3
                else:
                    letras_por_agregar =  "ku"
                    indice_letra -= 1
            else:
                letras_por_agregar =  "ku"
                indice_letra -= 1
        elif letra2 in "aeio":
            letras_por_agregar =  "k" + letra2
        else:
            letras_por_agregar =  "ku"
            indice_letra -= 1
    else:
        letras_por_agregar =  "ku"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_c(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra2 = palabra[indice_letra]
        if letra2 in "aou":
            letras_por_agregar =  "k" + letra2
        elif letra2 in "ei":
            letras_por_agregar =  "s" + letra2
        elif letra2 == "h":
            indice_letra += 1
            if indice_letra < len(palabra):
                letra3 = palabra[indice_letra]
                if letra3 in "aeiou":
                    letras_por_agregar = ch + letra3
                else:
                    letras_por_agregar =  ch + "u"
                    indice_letra -= 1
            else:
                letras_por_agregar =  ch + "u"
                indice_letra -= 1
        else:
            letras_por_agregar =  "ku"
            indice_letra -= 1
    else:
        letras_por_agregar =  "ku"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_g(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra2 = palabra[indice_letra]
        if letra2 in "aou":
            letras_por_agregar =  "g" + letra2
        elif letra2 in "ei":
            letras_por_agregar =  "j" + letra2
        else:
            letras_por_agregar =  "gu"
            indice_letra -= 1
    else:
        letras_por_agregar =  "gu"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_l(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra2 = palabra[indice_letra]
        if letra2 == "l":
            indice_letra += 1
            if indice_letra < len(palabra):
                letra3 = palabra[indice_letra]
                if letra3 in "aeiou":
                    letras_por_agregar = "y" + letra3
                else:
                    letras_por_agregar =  "yu"
                    indice_letra -= 1
            else:
                letras_por_agregar =  "ru"
                indice_letra -= 1
        elif letra2 in "aeiou":
            letras_por_agregar =  "r" + letra2
        else:
            letras_por_agregar =  "ru"
            indice_letra -= 1
    else:
        letras_por_agregar =  "ru"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_n(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra2 = palabra[indice_letra]
        if letra2 in "aeiou":
            letras_por_agregar = "n" + letra2
        else:
            letras_por_agregar = "nn"
            indice_letra -= 1
    else:
        letras_por_agregar = "nn"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_t(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra = palabra[indice_letra]
        if letra in "aeiou":
            letras_por_agregar = "t"+letra
        else:
            letras_por_agregar = "to"
            indice_letra -= 1
    else:
        letras_por_agregar = "to"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_d(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra = palabra[indice_letra]
        if letra in "aeiou":
            letras_por_agregar = "d"+letra
        elif letra in " ":
            letras_por_agregar = "xdo"
            indice_letra -= 1
        else:
            letras_por_agregar = "do"
            indice_letra -= 1
    else:
        letras_por_agregar = "xdo"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_y(palabra, indice_letra):
    indice_letra += 1
    if indice_letra < len(palabra):
        letra = palabra[indice_letra]
        if letra in "aeiou":
            letras_por_agregar = "y"+letra
        else:
            letras_por_agregar = "i"
            indice_letra -= 1
    else:
        letras_por_agregar = "i"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)

def manejar_letra(palabra, indice_letra):
    letra = palabra[indice_letra]
    indice_letra += 1
    if indice_letra < len(palabra):
        letra2 = palabra[indice_letra]
        if letra2 in "aeiou":
            letras_por_agregar = letra + letra2
        else:
            letras_por_agregar = letra + "u"
            indice_letra -= 1
    else:
        letras_por_agregar = letra + "u"
        indice_letra -= 1
    return (letras_por_agregar, indice_letra)


def palabra_a_sonoridad(palabra):
    palabra = palabra.lower().replace("z", "s").replace("rr", "r").replace("x", "kus")
    palabra = reemplazar_tildes(palabra)
    nueva_palabra = ""
    indice_letra = -1
    while indice_letra < len(palabra):
        indice_letra += 1
        if indice_letra >= len(palabra):
            continue
        letra = palabra[indice_letra]
        if letra in "aeiou":
            nueva_palabra += letra
        elif letra in "wrpsfjkbm":
            letras_por_agregar, indice_letra = manejar_letra(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == "q":
            letras_por_agregar, indice_letra = manejar_q(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == "c":
            letras_por_agregar, indice_letra = manejar_c(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == "g":
            letras_por_agregar, indice_letra = manejar_g(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == "l":
            letras_por_agregar, indice_letra = manejar_l(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == "n":
            letras_por_agregar, indice_letra = manejar_n(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == 't':
            letras_por_agregar, indice_letra = manejar_t(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == 'd':
            letras_por_agregar, indice_letra = manejar_d(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == 'y':
            letras_por_agregar, indice_letra = manejar_y(palabra, indice_letra)
            nueva_palabra += letras_por_agregar
        elif letra == "h":
            continue
        elif letra == "v":
            nueva_palabra += "b"
        elif letra == "ñ":
            nueva_palabra += ny
        elif letra == " ":
            nueva_palabra += " "
        else:  # otro caracter
            nueva_palabra += letra
    return nueva_palabra


def traducir(palabra):
    """
    Funcion que japoniza una palabra en espanol
    :param palabra:
    :return (palabra_fonetica, palabra_traducida):
    """
    palabra = palabra_a_sonoridad(palabra)
    palabra_traducida = ""
    indice_letra = -1
    while indice_letra < len(palabra):
        indice_letra += 1
        if indice_letra >= len(palabra):
            continue
        letra = palabra[indice_letra]
        if letra in "aeioux":
            palabra_traducida += diccionario[letra]
        else:
            try:
                indice_letra += 1
                letra2 = palabra[indice_letra]
                palabra_traducida += diccionario[letra + letra2]
            except KeyError:
                indice_letra -= 1
                palabra_traducida += letra
            except IndexError:
                palabra_traducida += letra

    return (palabra.replace(ch, 'ch').replace('nn', 'n').replace(ny, "ny").
            replace('si', 'shi').replace('x', 'd'), palabra_traducida)

if __name__ == '__main__':
    while 1:
        palabra = input("ingresa una palabra: ")
        print("sonido palabra:", traducir(palabra))
