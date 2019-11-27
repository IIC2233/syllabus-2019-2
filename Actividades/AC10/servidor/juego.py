from random import choice


class Juego:

    def crear_tablero(self):
        '''Crea matriz de tablero.'''
        self.tablero = [[' ' for _ in range(7)] for _ in range(6)]
        self.alturas = [0] * 7

    def tablero_string(self):
        '''Retorna el tablero en forma de string para ser impreso.'''
        fila_indices = [str(indice) for indice in range(7)]
        filas = list(reversed(self.tablero)) + [fila_indices]
        return '\n'.join(f' | {" | ".join(fila)} | ' for fila in filas)

    def es_jugada_valida(self, columna):
        '''Chequea que un número de columna sea una jugada válida.'''
        return 0 <= columna <= 6 and columna in self.obtener_columnas_validas()

    def turno_jugador(self, jugada):
        '''Ejecuta el turno del jugador y revisa si ganó.'''
        return self.agregar_casilla('a', jugada)

    def turno_cpu(self):
        '''Ejecuta el turno del CPU y revisa si ganó.'''
        jugada = choice(self.obtener_columnas_validas())
        return self.agregar_casilla('e', jugada)

    def empate(self):
        '''Chequea que no queden jugadas válidas restantes.'''
        return len(self.obtener_columnas_validas()) == 0

    def obtener_columnas_validas(self):
        '''Retorna las columnas válidas del tablero.'''
        return [columna for columna in range(7) if self.alturas[columna] < 6]

    def agregar_casilla(self, caracter, columna):
        '''Agrega ficha de un jugador en cierta columna.'''
        fila = self.alturas[columna]
        self.tablero[fila][columna] = caracter
        self.alturas[columna] += 1
        return self.chequear_ganador(caracter, (columna, fila))

    def chequear_casilla(self, posicion_x, posicion_y, caracter, acumulado, direccion, sentido):
        '''Chequea cuantas veces seguidas se repite un caracter.'''
        x, y = direccion
        try:
            posicion_x += x * sentido
            posicion_y += y * sentido
            if self.tablero[posicion_y][posicion_x] == caracter:
                acumulado += 1
                if acumulado > 4:
                    return acumulado
                else:
                    return self.chequear_casilla(posicion_x, posicion_y, caracter, acumulado,
                                                 direccion, sentido)
            else:
                return acumulado
        except IndexError:
            return acumulado

    def chequear_ganador(self, caracter, posicion):
        '''Chequea si la variable caracter formo 4 en linea.'''
        x, y = posicion
        if self.tablero[y][x] == caracter:
            for direccion in [(0, 1), (1, 1), (1, 0), (1, -1)]:
                if self.chequear_casilla(x, y, caracter, 1, direccion, 1) \
                        + self.chequear_casilla(x, y, caracter, 0, direccion, -1) >= 4:
                    return True
