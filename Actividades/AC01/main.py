from recuperar_bd import recuperar_archivo, guardar_archivo
from banco_seguro import BancoSeguroDCC
from os import path

'''
Estas lineas de codigo son para que puedas ir probando
las cosas que vas implementando, queda a tu criterio
si quieres cambiar algunas lineas
'''


# Primero es el proceso de recuperar los archivos, desencriptamos ambos

clientes_desencriptado = recuperar_archivo(path.join('bd_encriptada', 'clientes.txt'))
transacciones_desencriptado = recuperar_archivo(path.join('bd_encriptada', 'transacciones.txt'))


# Con la siguiente funcion, se crea clientes.txt en la carpeta banco seguro

guardar_archivo(path.join('banco_seguro', 'clientes.txt'), clientes_desencriptado)

# Nota que no guardamos transacciones, esto es porque solo se necesitará la lista

# Una vez recuperada la informacion ...

# Creamos al banco y a los clientes

banco_dcc_seguro = BancoSeguroDCC()
banco_dcc_seguro.cargar_clientes(path.join('banco_seguro', 'clientes.txt'))

# Descubriremos a los clientes falsos
'''
Aquí usamos la informacion recuperada de transacciones. Pero ¿Cuando se guarda
entonces la información en banco seguro/transacciones.txt? Recuerda que
retiro y deposito_seguro guardan informacion en dicho archivo. Una buena idea
es usar estos métodos al momento de verificar el historial
'''
banco_dcc_seguro.verificar_historial_transacciones(transacciones_desencriptado[1:])

banco_dcc_seguro.validar_monto_clientes(path.join('banco_seguro', 'clientes.txt'))

# Llego la hora de desenmascarar a los tramposos
print('Los clientes tramposos son:')
for cliente in banco_dcc_seguro.clientes:
    if cliente.tiene_fraude:
        print(cliente)
