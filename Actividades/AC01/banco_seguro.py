from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        # completar
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        # completar
        pass

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        '''
        Completar: Recuerda que si el saldo es menor a 0, entonces este cliente
        si tiene un fraude
        '''
        pass

    def deposito_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            # completar
            pass

    def retiro_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            # completar
            pass


class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        # completar
        pass

    def cargar_clientes(self, ruta):
        # completar
        pass

    def realizar_transaccion(self, id_cliente, dinero, accion):
        # completar
        pass

    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        # completar
        pass

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        # completar
        pass
