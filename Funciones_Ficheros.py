# Module with functions for files

# Creating files with movementes record
def crearFicheros():
    fO=open('historialO.txt', 'w')
    fO.write("HISTORIAL DE MOVIMIENTOS - JUGADOR O:" + "\n")
    fO.close()

    fX=open('historialX.txt', 'w')
    fX.write("HISTORIAL DE MOVIMIENTOS - JUGADOR X:" + "\n")
    fX.close()

# Add movement to the record file for Player 'O'
def añadirJugadaO(mov):
    f=open('historialO.txt', 'a')
    txt="Fo: " + str(mov[0]) + "; Co: " + str(mov[1]) + "; Ff: " + str(mov[2]) + "; Cf: " + str(mov[3])
    f.write(txt + "\n")
    f.close()

# Add movement to the record file for Player 'X'
def añadirJugadaX(mov):
    f=open('historialX.txt', 'a')
    txt="Fo: " + str(mov[0]) + "; Co: " + str(mov[1]) + "; Ff: " + str(mov[2]) + "; Cf: " + str(mov[3])
    f.write(txt + "\n")
    f.close()

