import socket
import json
import pickle

class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = None
        self.port = None
        self.socket_cliente = None
        try:
            # Aqui deberas intentar conectar al servidor.

            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        bytes_recibidos = self.socket_cliente.recv(100) # Rayos, esto es demasiado poco

        # Debe haber un string para imprimirse
        mensaje = None
        # Debe haber un boolean para saber si continuar funcionando
        continuar = None

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar

        return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        mensaje_codificado = accion.encode('utf-8')

        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
