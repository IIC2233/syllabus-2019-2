"""
server.py -- un simple servidor
"""
import pickle
from socket import socket
import os

from PyQt5.QtCore import QRect

HOST = '127.0.0.1'


class Servidor:
    """
    Una clase que representa un servidor.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.cliente = None
        self.socket = socket()

    def run(self):
        """
        Enciende el servidor que puede conectarse
        y recibir comandos desde un único cliente.
        """

        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Escuchando en {self.host}:{self.port}.")

        while self.cliente is None:
            self.cliente, _ = self.socket.accept()
            print("¡Un cliente se ha conectado!")
            while self.cliente:
                comando = pickle.loads(self.receive())
                if comando == 'descargar':
                    self.enviar_archivo('doggo.jpg')
                elif comando == 'ls':
                    self.lista_directorio()

        print("Arrivederci.")

    def send(self, mensaje):
        """
        Envía datos binarios al cliente conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        self.cliente.sendall(int.to_bytes(len(mensaje), byteorder='big', length=4))
        self.cliente.sendall(mensaje)

    def receive(self):
        """
        Recibe datos binarios del cliente, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        numero_de_bytes = int.from_bytes(self.cliente.recv(4), byteorder='big')
        message = bytearray()
        while numero_de_bytes > 0:
            largo_por_recibir = min(numero_de_bytes, 2048)
            message.extend(self.socket.recv(largo_por_recibir))
            numero_de_bytes -= 2048
        return message

    def lista_directorio(self):
        """
        Envía al cliente una lista que contiene los nombres de
        todos los archivos existentes en la carpeta del servidor.
        """
        print(os.listdir('.'))
        message = pickle.dumps(os.listdir('.'))
        self.send(message)

    def enviar_archivo(self, ruta_archivo):
        """
        Envía al cliente un archivo ubicado en el directorio del servidor.
        """
        with open(ruta_archivo, 'rb') as file:
            data = file.read()
        self.send(data)

    def desconectar(self):
        self.cliente = None
        print("El cliente se ha desconectado.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    servidor = Servidor(int(port_))
    servidor.run()
