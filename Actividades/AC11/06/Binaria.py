# Diccionario ASCII para obtener las letras correspondientes.
ascii_letters_dic = {i: chr(i) for i in range(32, 123)}

# Obten los datos del archivo magnezone.pkmn

def obtener_movimiento_efectivo(path):
	# Obten los datos desde path y usa el algoritmo
	# COMPLETAR
	pass


# El mensaje que debe escribir, debe generar tu victoria. 
# Cualquier otro resultado hara que gane el lider de gimnasio.

if __name__ == "__main__":
	try:
		mensaje = obtener_movimiento_efectivo("magnezone.pkmn")
		if mensaje:
			print(mensaje)
		else:
			print("MAGNEZONE ha usado Trueno! Tu PIDGEOT ha sido debilitado. No te quedan más PROGRáMONS")
	except Exception as err:
		print(err)
		print("MAGNEZONE ha usado Trueno! Tu PIDGEOT ha sido debilitado. No te quedan más PROGRáMONS")
