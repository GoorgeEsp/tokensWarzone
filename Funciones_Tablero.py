# Module with functions related to the tabletop matrix

# FUNCTION IN CHARGE OF CREATING THE INITIAL BOARD
def crearTablero():
    # To define the board we will use a matrix, that is, a list of lists
    T = []
    # Representing empty board
    for i in range(8):
        T.append(['-'] * 8)

    # Añadimos las fichas al tablero
    for i in range(len(T)):
        # Add 'X' to the board
        if i == 0 or i == 2:
            for j in range(8):
                if j%2 == 1 :
                    T[i][j] = 'X'
        elif i == 1 :
            for j in range(8):
                if j%2 == 0 :
                    T[i][j] = 'X'
        # Add 'O' to the board
        elif i == 5 or i == 7 :
            for j in range(8):
                if j%2 == 0 :
                    T[i][j] = 'O'
        elif i == 6  :
            for j in range(8):
                if j%2 == 1 :
                    T[i][j] = 'O'
    return T

# Print the board
def imprimirTablero(T):
    for linea in T:
        print(linea)

# Print the board on screen pretty
def imprimirTableroBonito(T):
    print(" ", end =" ")
    for i in range(len(T)):
        print(i, end =" ")
    print("")
    for i in range(len(T)):
        print(i, end =" ")
        for j in range(len(T)):
            print (T[i][j], end=" ")
        print()
    print()

# Modifies board
def modificarTablero(T, mov):
    T[mov[2]][mov[3]]=T[mov[0]][mov[1]]
    T[mov[0]][mov[1]]="-"
    return T

