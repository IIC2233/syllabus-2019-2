'''
Clases ya implementadas, no tocar
'''


class Cliente:
    def __init__(self, id_cliente, nombre, contrasena):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.saldo = 0  # Se asume que el cliente tiene saldo 0
        self.contrasena = contrasena

    def __str__(self):
        return f"Nombre: {self.nombre}, Saldo: {self.saldo}, ID Cliente: {self.id_cliente}"

    def depositar(self, dinero):
        self.saldo += dinero

    def retirar(self, dinero):
        self.saldo -= dinero


class BancoDCC:
    def __init__(self):
        self.clientes = []

    def cargar_clientes(self, ruta):
        with open(ruta, "r", encoding="UTF-8") as file:
            for line in file:
                id_cliente, nombre, saldo, contrasena = line.strip().split(",")
                # Notar que dejamos el id como string, no hay problema
                # mientras se sea consistente
                instancia_cliente = Cliente(id_cliente, nombre,
                                            contrasena)
                self.clientes.append(instancia_cliente)

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        print(f"Cliente con id {id_cliente} no encontrado")
        return None
