__author__ = "chapito96 & fringlesinthestreet" + " & StroveLight"

import threading
import socket
import json
from traductor import traducir

class Server:

    '''
    Esta es la clase encargada de montar el servidor y realizar las operaciones
    lógicas necesarias para el funcionamiento del sistema
    '''

    def __init__(self):
        print("Inicializando servidor...")
        # Primero se crea un diccionario de los sockets
        self.sockets = dict()

        # Ponemos la dirección donde va a estar situado nuestro servidor
        # El localhost representa "esta computadora" en cualquier red.
        self.host = "localhost"

        # Definimos un puerto al cual el servidor va a estar escuchando
        self.port = 1238

        # Inicializar socket principal del servidor.
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # El método bind enlaza el servidor con el puerto y la dirección.
        # Cualquier cosa que llegue al puerto antes puesto va a ser 'escuchado' por
        # el servidor
        self.socket_servidor.bind((self.host, self.port))
        print("Dirección y puerto enlazados..")

        # Luego, con el método listen hacemos que el servidor escuche conexiones
        # entrantes. Se le puede pasar como argunento un numero entero, el cual
        # representa el número de conexiones máxima que va a tener en espera de ser aceptadas.
        # En este caso no se puso un argumento, ya que no se necesita una restriccion de esto
        self.socket_servidor.listen()
        print("Servidor escuchando en {}:{}...".format(self.host, self.port))

        # Inicializamos un thread para aceptar conexiones entrantes. Es útil
        # usar un thread para que el programa pueda realizar otras cosas
        # por mientras que acepta conexiones
        thread = threading.Thread(target=self.accept_connections_thread, daemon=True)
        thread.start()
        print("Servidor aceptando conexiones...")


    def accept_connections_thread(self):
        '''
        Este método es utilizado en el thread para ir aceptando conexiones de
        manera asíncrona al programa principal
        :return:
        '''
        # primero se indica un id para guardar cada cliente distinto
        id_ = 1
        while True:

            # El método accept espera (queda esperando) hasta que algún cliente
            # se conecte y luego retorna una tupla con el socket del cliente
            # recién conectado y la dirección de ésto.
            # Nosotros sólo guardamos el socket.
            client_socket, _ = self.socket_servidor.accept()

            # Luego, se guarda el socket
            self.sockets[id_] = client_socket


            print("Servidor conectado a un nuevo cliente...")

            # inicializamos un thread para escuchar a la conexión recién aceptada
            # Por lo que cada cliente conectado va a tener su propio Thread
            # escuchándolo.
            # Pasamos como argumento el socket actual y el id del cliente
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, id_),
                daemon=True
            )
            listening_client_thread.start()

            # Finalmente se cambia el valor del id_para evitar repeticiones
            id_ += 1

    def listen_client_thread(self, client_socket, id_cliente):
        '''
        Este método va a ser usado múltiples veces en threads pero cada vez con
        sockets de clientes distintos.
        :param client_socket: objeto socket correspondiente a algún cliente
        :return:
        '''

        while True:
            try:
                # Primero recibimos los 4 bytes del largo
                response_bytes_length = client_socket.recv(4)
                # Los decodificamos
                response_length = int.from_bytes(response_bytes_length,
                                                 byteorder="big")

                # Luego, creamos un bytearray vacío para juntar el mensaje
                response_bytes = bytearray()

                # Recibimos datos hasta que alcancemos la totalidad de los datos
                # indicados en los primeros 4 bytes recibidos.
                while len(response_bytes) < response_length:
                    largo_por_recibir = min(response_length - len(response_bytes), 256)
                    response_bytes += client_socket.recv(largo_por_recibir)

                # Una vez que tenemos todos los bytes, entonces ahí decodificamos
                response = response_bytes.decode()

                # Luego, debemos cargar lo anterior utilizando json
                decoded = json.loads(response)

                # Para evitar hacer muy largo este método, el manejo del mensaje se
                # realizará en otro método
                self.manejar_comando(decoded, client_socket)
            except ConnectionResetError:  # Es decir, si el cliente se desconecta
                del self.sockets[id_cliente]
                break

    def manejar_comando(self, recibido, socket):
        '''
        Este método toma lo recibido por el cliente correspondiente al socket pasado
        como argumento.
        :param received: diccionario de la forma: {"palabra": Palabra recibida}
        :param client_socket: socket correspondiente al cliente que envió el mensaje
        :return:
        '''

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(recibido))

        palabra = recibido['palabra']
        palabra_fonetica, palabra_traducida = traducir(palabra)

        mensaje = {"propio": True,
                   "original": palabra,
                   "fonetica": palabra_fonetica,
                   "traducida": palabra_traducida}

        # primero le enviamos la respuesta al que pidio la conversion
        self.send(mensaje, socket)

        # despues le actualizamos la ultima consulta a todas los clientes
        mensaje.update({"propio": False})
        self.sendall(mensaje)

    # Usaremos el método send() para enviar mensajes hacia algún socket cliente.
    # Debemos implementar en este método el protocolo de comunicación donde los
    # primeros 4 bytes indicarán el largo del mensaje.
    @staticmethod
    def send(mensaje, socket):
        '''
        Este método envía la información al cliente correspondiente al socket.
        :param msg: diccionario del tipo {"mensaje": contenido del mensaje}
        :param socket: socket del cliente al cual se le enviará el mensaje
        :return:
        '''

        # Le hacemos json.dumps y luego lo transformamos a bytes
        msg_json = json.dumps(mensaje)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        socket.send(msg_length + msg_bytes)

    def sendall(self, mensaje):
        # primero se copian las id de los sockets
        id_sockets = list(self.sockets.keys())[:]
        # y luego se iteran sobre ellos
        for id_ in id_sockets:
            try:
                self.send(mensaje, self.sockets[id_])
            except ConnectionResetError:
                del self.sockets[id_]
                print('Error de conexion con cliente')
            except ConnectionAbortedError:
                del self.sockets[id_]
                print('Error de conexion con cliente')
            except IndexError:
                print('Ya se ha eliminado el cliente del diccionario')


if __name__ == "__main__":

    server = Server()

    # Se mantiene al servidor corriendo
    while True:
        pass
