import socket
import json
import pickle
from juego import Juego


class Servidor:

    def __init__(self):
        '''Inicializador de servidor.

        Crea socket de servidor, lo vincula a un puerto.'''
        # -----------------------------------------
        # Completar y agregar argumentos desde aquí

        self.host = None
        self.port = None
        self.socket_servidor = None

        # Aqui deberas preparar el socket para que escuche una conexion

        # Completar y agregar argumentos hasta aquí
        # -----------------------------------------
        print("Servidor iniciado.")
        self.juego = None  # Juego comienza nulo.
        self.socket_cliente = None  # Aún no hay cliente.

    def esperar_conexion(self):
        '''Espera a la conectarse con un cliente y obtiene su socket.'''
        print("Esperando cliente...")
        # --------------------
        # Completar desde aquí

        # Debes actualizar el valor de self.socket_cliente al conectar

        # Completar hasta aquí
        # --------------------
        print("¡Servidor conectado a cliente!")
        self.interactuar_con_cliente()

    def interactuar_con_cliente(self):
        '''Comienza ciclo de interacción con cliente.

        Recibe un acción y responde apropiadamente.'''
        self.enviar_estado('', True)
        while self.socket_cliente:
            accion = self.recibir_accion()
            self.manejar_accion(accion)

    def enviar_estado(self, mensaje, continuar):
        '''Envia estado del juego en el servidor.'''
        if continuar:
            if self.juego is not None:
                mensaje = f'{self.juego.tablero_string()}\n{mensaje}\n'
            acciones = ("¿Qué deseas hacer?\n"
                        "Para jugar nuevo juego: \\juego_nuevo\n"
                        "Para jugar en una columna: \\jugada columna\n"
                        "Para salir: \\salir\n")
            mensaje = mensaje + acciones
        # -----------------------------------------------------
        # Completar y usar un metodo para todo largo de mensaje

        mensaje_codificado = None

        # Completar hasta aquí
        # --------------------

    def recibir_accion(self):
        '''Recibe mensaje desde el cliente y lo decodifica.'''
        # -----------------------------------------------------
        # Completar y usar un metodo para todo largo de mensaje

        bytes_recibidos = self.socket_cliente.recv(100)  # Rayos, esto es demasiado po

        accion = None  # Respuesta resultante

        # Completar hasta aquí
        # --------------------
        return accion

    def manejar_accion(self, accion):
        '''Maneja la acción recibida del cliente.'''
        print(f'Acción recibida: {accion}')
        # --------------------
        # Completar desde aquí

        tipo = None  # Obtener el tipo de acción que envió el cliente.

        # Completar hasta aquí
        # --------------------
        if tipo == '\\juego_nuevo':
            self.juego = Juego()
            self.juego.crear_tablero()
            self.enviar_estado('', True)
        elif tipo == '\\salir':
            self.enviar_estado('¡Adios!', False)
            self.juego = None
            self.socket_cliente.close()
            print('Cliente desconectado.\n')
            self.socket_cliente = None
        elif tipo == '\\jugada':
            if self.juego is None:
                self.enviar_estado('Ningún juego ha iniciado.', True)
            else:
                # --------------------
                # Completar desde aquí

                # Obtener la jugada que envió el cliente.
                jugada = None

                # Completar hasta aquí
                # --------------------
                if not self.juego.es_jugada_valida(jugada):
                    self.enviar_estado('Jugada inválida.', True)
                else:
                    gano = self.juego.turno_jugador(jugada)
                    if gano:
                        self.enviar_estado('¡Ganaste! Se acabó el juego.', True)
                        self.juego = None
                    else:
                        perdio = self.juego.turno_cpu()
                        if perdio or self.juego.empate():
                            self.enviar_estado('No ganaste :( Se acabó el juego.', True)
                            self.juego = None
                        else:
                            self.enviar_estado('', True)


if __name__ == "__main__":
    servidor = Servidor()
    while True:
        try:
            servidor.esperar_conexion()
        except KeyboardInterrupt:
            print("\nServidor interrumpido")
            break
