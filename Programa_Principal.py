# Main program

import winsound
import random
from Funciones_Tablero import *
from Funciones_Control import *
from Funciones_Aleatorio import *
from Funciones_Ficheros import *



# Creates files with game record
crearFicheros()


# Raffle who starts playing
empieza = decidirInicial()
print()


# Start game and show board
T = crearTablero()
imprimirTableroBonito(T)


# Initializating game
partidaTerminada = False

if empieza == False:
    while partidaTerminada == False:
        # Movement player 'O'
        T = turnoO(T)
        if quedanFichasX(T) == False:
            partidaTerminada = True
            break

        # Movement player 'X'
        T = turnoX(T)
        if quedanFichasO(T) == False:
            partidaTerminada = True


elif empieza == True:
    while partidaTerminada == False:
        # Movement player 'X'
        T = turnoX(T)
        if quedanFichasO(T) == False:
            partidaTerminada = True
            break

        # Movement player 'O'
        T = turnoO(T)
        if quedanFichasX(T) == False:
            partidaTerminada = True


# Shows end of game
if quedanFichasX(T) == False:
    victoriaO()
elif quedanFichasO(T) == False:
    victoriaX()

