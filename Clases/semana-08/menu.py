from abc import ABC
from os import path

class Menu(ABC):

    def __init__(self):
        self.funcionando = True
        self.opciones = [
            # (nombre_opcion, funcion_opcion)
            ("Salir", self.salir)
        ]

    def __mostrar_menu(self):
        for i, opcion in enumerate(self.opciones):
            print(f"{i+1}) {opcion[0]}")

    def comenzar(self):
        while self.funcionando:
            self.pedir_input()
            print()

    def salir(self):
        self.funcionando = False
        print("Saliendo de menú.")

    def revisar_input_opcion(self, seleccion):
        if not seleccion.isdigit():
            raise ValueError("Input no es un número")
        if int(seleccion) > len(self.opciones) or int(seleccion) < 1:
            raise KeyError("No es una opción válida")

    def pedir_input(self):
        try:
            self.__mostrar_menu()
            seleccion = input("Ingresar opción: ")
            print()
            self.revisar_input_opcion(seleccion)
        except (ValueError, KeyError) as error:
            print(f"Error: {error}")
            print("Intente de nuevo")
        else:
            seleccion = int(seleccion)
            self.opciones[seleccion - 1][1]()

    # def pedir_input(self): # Caso sin excepciones y solo con ifs/else
    #     self.__mostrar_menu()
    #     seleccion = input("Ingresar opción: ")
    #     print()
    #     if seleccion.isdigit():
    #         seleccion = int(seleccion)
    #         if len(self.opciones) >= seleccion >= 1:
    #             self.opciones[seleccion - 1][1]()
    #         else:
    #             print("Error: Debes ingresar una opción válida")
    #             print("Intente de nuevo")    
    #     else:
    #         print("Error: Debes ingresar un número")
    #         print("Intente de nuevo")


class MenuInicial(Menu):

    def __init__(self):
        super().__init__()
        self.opciones = [
            ("Ingresar nombre usuario", self.ingresar_nombre_usuario),
            ("Ingresar base de datos", self.ingresar_base_de_datos),
        ] + self.opciones

    def ingresar_nombre_usuario(self):
        try:
            nombre = input("Ingresar nombre de usuario: ")
            print()
            self.revisar_nombre_valido(nombre)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"{nombre} guardado como nombre.")
    

    def ingresar_base_de_datos(self):
        try:
            archivo = input("Ingresar archivo de base de datos: ")
            print()
            self.revisar_archivo_existente(archivo)
        except FileNotFoundError as error:
            print(f"Error: {error}")
        else:
            print(f"{archivo} guardado como base de datos.")
    

    def revisar_nombre_valido(self, input_recibido):
        if not input_recibido.islower():
            raise ValueError("Solo deben contener caracteres en minúscula")
    
        if " " in input_recibido:
            raise ValueError("No debe contener espacios")

    def revisar_archivo_existente(self, input_recibido):
        if not path.exists(input_recibido):
            raise FileNotFoundError(f"Archivo {input_recibido} no existe.")


if __name__ == '__main__':
    menu = MenuInicial()
    menu.comenzar()
