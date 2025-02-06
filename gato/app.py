import tablero

def main():
    
    numeros = [str(i) for i in range(1,10)]
    corriendo = True
    X = {"G":0, "P":0, "E":0}
    O = {"G":0, "P":0, "E":0}
    score = {"X":X, "O":O}
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score, g)
        tablero.despliegatablero(score)
if __name__ == '__main__':
    main()
