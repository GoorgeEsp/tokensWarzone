# Module with control functions

import winsound
from Funciones_Tablero import *
from Funciones_Ficheros import *



# Ask player for movement
def pedirMovimiento():
    mov=[]
    mov.append(int(input("Fila de origen: ")))
    mov.append(int(input("Columna de origen: ")))
    mov.append(int(input("Fila de destino: ")))
    mov.append(int(input("Columna de destino: ")))
    return mov

# Checks movement for 'O' player
def verificarMovimientoO(T, mov):
    # Check token out of board
    if mov[2] >= len(T) or mov[3] >= len(T):
        return False
    if mov[2] < 0 or mov[3] < 0:
        return False
    if T[mov[0]][mov[1]] == T[mov[2]][mov[3]]:
        return False

    # Check token just move one horizontal square 
    if not (mov[3] == mov[1]+1 or mov[3] == mov[1]-1):
        return False
    # Check token just move one vertical square 
    if not (mov[2] == mov[0]+1 or mov[2] == mov[0]-1):
        return False

    # Check movement right
    if T[mov[0]][mov[1]] != "O":
        return False
    if T[mov[2]][mov[3]] == "O":
        return False

    return True

# Checks movement for 'X' player
def verificarMovimientoX(T, mov):
    # Check token out of board
    if mov[2] >= len(T) or mov[3] >= len(T):
        return False
    if mov[2] < 0 or mov[3] < 0:
        return False
    if T[mov[0]][mov[1]] == T[mov[2]][mov[3]]:
        return False

    # Check token just move one horizontal square
    if not (mov[3] == mov[1]+1 or mov[3] == mov[1]-1):
        return False
    # Check token just move one vertical square
    if not (mov[2] == mov[0]+1 or mov[2] == mov[0]-1):
        return False

    # Check movement right
    if T[mov[0]][mov[1]] != "X":
        return False
    if T[mov[2]][mov[3]] == "X":
        return False

    return True

# Player's 'O' turn
def turnoO(T):
    winsound.PlaySound('Bell1.wav', winsound.SND_FILENAME)
    print("Mueve ficha el Jugador 'O'")
    mov=pedirMovimiento()
    while verificarMovimientoO(T, mov) == False:
        print("Movimiento no válido")
        mov=pedirMovimiento()
    # Modify and print board with new movement
    print()
    T=modificarTablero(T, mov)
    imprimirTableroBonito(T)
    # Add movement to file
    añadirJugadaO(mov)
    return T

# Player's 'X' turn
def turnoX(T):
    winsound.PlaySound('Bell1.wav', winsound.SND_FILENAME)
    print("Mueve ficha el Jugador 'X'")
    mov=pedirMovimiento()
    while verificarMovimientoX(T, mov) == False:
        print("Movimiento no válido")
        mov=pedirMovimiento()
    # Modify and print board with new movement
    print()
    T=modificarTablero(T, mov)
    imprimirTableroBonito(T)
    # Add movement to file
    añadirJugadaX(mov)
    return T

# Check if 'O' tokens remaining
def quedanFichasO(T):
    for i in T:
        for j in i:
            if j == 'O':
                return True
    return False

# Check if 'X' tokens remaining
def quedanFichasX(T):
    for i in T:
        for j in i:
            if j == 'X':
                return True
    return False

# Win for player 'O'
def victoriaO():
    winsound.PlaySound('fanfarria.wav', winsound.SND_FILENAME)
    print("El Jugador 'O' ha ganado")

# Win for player 'X'
def victoriaX():
    winsound.PlaySound('fanfarria.wav', winsound.SND_FILENAME)
    print("El Jugador 'X' ha ganado")


