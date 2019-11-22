"""
client.py -- un simple cliente
"""

import pickle
from socket import socket, SHUT_RDWR

HOST = '127.0.0.1'


class Cliente:
    """
    Una clase que representa un cliente.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.socket = socket()
        self.connected = False

    def run(self):
        """
        Enciende el cliente que puede conectarse
        para enviar algunos comandos al servidor.
        """

        self.socket.connect((self.host, self.port))
        self.connected = True

        while self.connected:

            comando = input('Ingresa un comando: ')

            self.send(pickle.dumps(comando))

            if comando == 'descargar':
                self.descargar('doggo.jpg')
            elif comando == 'ls':
                self.ls()

    def send(self, mensaje):
        """

        Envía datos binarios al servidor conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        self.socket.sendall(int.to_bytes(len(mensaje), byteorder='big', length=4))
        self.socket.sendall(mensaje)

    def receive(self):
        """
        [COMPLETAR]
        Recibe datos binarios del servidor, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        numero_de_bytes = int.from_bytes(self.socket.recv(4), byteorder='big')
        message = bytearray()
        while numero_de_bytes > 0:
            largo_por_recibir = min(numero_de_bytes, 2048)
            message.extend(self.socket.recv(largo_por_recibir))
            numero_de_bytes -= 2048
        return message


    def ls(self):
        """
        Este comando recibe una lista con los archivos del servidor.
        """
        data = self.receive()
        data2 = pickle.loads(data)
        for archivo in data2:
            print(' -', archivo)


    def descargar(self, ruta_archivo):
        """
        Este comando recibe un archivo ubicado en el servidor.
        """
        data = self.receive()
        if not data:
            print('Archivo no existente')
            return
        with open(ruta_archivo, 'wb') as file:
            file.write(data)
        print('Archivo creado')

    def cerrar_sesion(self):
        self.connected = False
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()
        print("Arrivederci.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    cliente = Cliente(int(port_))
    cliente.run()
