import json
import pickle
import random


class Programon:
	def __init__(self, nombre, movimientos):
		self.nombre = nombre
		self.movimientos = movimientos
		self.origen = ''

	def __setstate__(self, state):
		# Esta sobrecarga te permitira personalizar la deserializacion pickle
		# Completar
		pass

	def __repr__(self):
		return f'{self.nombre} ({self.origen}): {self.movimientos}'



def programon_hook(dicto):
	# Esta funcion te permitira personalizar la deserializacion json
	# Completar
	pass

def obtener_programons_json(path):
	# Completar
	pass

def obtener_programons_pickle(path):
	# Completar
	pass


if __name__ == '__main__':
	moves = False
	load = False
	stolen = True
	your_team = []
	enzinni_team = []
	try:
		your_team = obtener_programons_json('programons_yours.json')
		if len(your_team) == 6 and len(your_team[5].movimientos) > 0:
			print('Has cargado a tu equipo')
			load = True
			moves = True
		elif len(your_team) == 6 and len(your_team[0].movimientos) == 0:
			print('Has cargado a tu equipo')
			load = True
		else:
			print('No has cargado a tu equipo completo.')
	except Exception as err:
		print(err)
		print('No has podido cargar a tu equipo. Has sido derrotado por default')

	try:
		enzinni_team = obtener_programons_pickle('programons_enzinni.teamp')
		print(enzinni_team)
		if len(enzinni_team) == 5:
			print('Se han devuelto los PROGRáMONS robados a sus dueños')
			stolen = False
		else:
			print('Se ha cargado los 151 PROGRáMONS de LÍDER ENZINNI')
	except Exception as err:
		print(err)
		print('Enzinni te envía a sus mafiosos. Has sido derrotado por default')

	if your_team and enzinni_team:
		your_team = your_team
		enzinni_team = enzinni_team
		e = enzinni_team[0]
		p = your_team[0]
		print('LÍDER ENZINNI envia a', e.nombre.capitalize())
		print('Ve!', p.nombre.capitalize())
		if not load:
			print('Luego de una ardua batalla, has perdido por no tener todos tus PROGRáMONS.')
		elif not moves:
			print(p.nombre.capitalize(), 'no le quedan más movimientos')
			print(p.nombre.capitalize(), 'uso combate')
			print('Luego de una ardua batalla, has perdido por no tener movimientos')
		elif stolen:
			print('No puedes con 151 PROGRáMONS, con suerte pudiste con 15. Has sido derrotado')
		else:
			print(p.nombre.capitalize(), 'uso', p.movimientos[0])
			print(e.nombre.capitalize(), 'uso', e.movimientos[0])
			print('...')
			e = enzinni_team[-1]
			p = your_team[-1]
			print(e.nombre.capitalize(), 'uso', e.movimientos[0])
			print(p.nombre.capitalize(), 'uso', p.movimientos[0])
			print(e.nombre.capitalize(), 'se ha debilitado.')
			print('Has derrotado a Líder ENZINNI')
