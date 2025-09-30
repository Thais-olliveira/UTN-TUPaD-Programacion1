"""
Ejercicio 9: Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
• Mostrar el tablero después de cada jugada.
"""
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print ("Tablero inicial:")
for fila in tablero:
    print(fila)
    
turno_jugador = 1
cantidad_jugadas = 0
ganador = False

while True:
    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))
    # Se la casilla ya esta ocupada o fuera de del tablero
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posicion invalida. Ingrese nuevamente.")
        continue
    
    if tablero[fila][columna] != '-':
        print("Posicion ocupada. Ingrese nuevamente.") 
        continue
    #Designa un signo para cada jugador
    ficha = None
    if turno_jugador == 1:
        ficha = 'X'
    else:
        ficha = 'O'

    tablero[fila][columna] = ficha

    print('Tablero actualizado:')
    for fila in tablero:
        print(fila)
    #Revisan las filas
    for i in range(3):
        if tablero[i][0] == ficha and tablero[i][1] == ficha and tablero[i][2] == ficha:
            print('El jugador', turno_jugador, 'ha ganado')
            ganador = True
            break
        #Revisan las columnas
        if tablero[0][i] == ficha and tablero[1][i] == ficha and tablero[2][i] == ficha:
            print('El jugador', turno_jugador, 'ha ganado')
            ganador = True
            break
    
    if ganador:
        break
    #Revisan las diagonales
    if tablero[0][0] == ficha and tablero[1][1] == ficha and tablero[2][2] == ficha:
        print('El jugador', turno_jugador, 'ha ganado')
        break
    if tablero[0][2] == ficha and tablero[1][1] == ficha and tablero[2][0] == ficha:
        print('El jugador', turno_jugador, 'ha ganado')
        break
    #Con 9 jugadas es empate
    cantidad_jugadas += 1
    if cantidad_jugadas == 9:
        print('Empate')
        break

    if turno_jugador == 1:
        turno_jugador = 2
    else:
        turno_jugador = 1
    print("Turno del jugador", turno_jugador)

print("Fin del juego")