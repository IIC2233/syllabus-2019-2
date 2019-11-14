def reparar_comunicacion(ruta):
    with open(ruta, 'rb') as bytes_file:
        pass
        # Procesar los bytes corrompidos

    with open('Docengelion.bmp', 'wb') as bytes_file:
        pass
        # Guardar los bytes arreglados

if __name__ == '__main__':
    try:
        reparar_comunicacion('EVA.xdc')
        print("PINTOSAR201: Comunicacion con pilotos ESTABLE")
    except Exception as error:
        print(f'Error: {error}')
        print("PINTOSAR301: CRITICO pilotos incomunicados DESCONEXION INMINENTE")