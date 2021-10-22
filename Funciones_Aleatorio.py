# Module random functions for game

import random

# Random start by coin flipping
def decidirInicial():
    # Coin flipping
    numero=random.randint(0,1)
    if numero == 0:
        lado="cara"
    if numero == 1:
        lado="cruz"

    print("Bienvenido a War Tokens. El jugador 1 jugará con las 'O' y el jugador 2 jugará con las 'X'")
    print("Vamos a sortear quien comienza jugando")

    # Ask player 1 to choose for face or cross
    j1=""
    while j1 != "cara" and j1 != "cruz":
        j1=input(print("Jugador 1, ¿quieres cara o cruz?"))
    # Choose winner
    if j1 == lado:
        ganador="Jugador 1"
        v=False
    else:
        ganador="Jugador 2"
        v=True

    print("El resultado fue", lado, "- Empieza", ganador)
    return v

