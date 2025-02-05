import tablero

def main():
    numeros = [str(i) for i in range(1,10)]	
    dsimbolos = {x:x for x in numeros}
    tablero.juego(dsimbolos)
    g = tablero.juego(dsimbolos)
    if g is not None:
        print(f'Gana: {g}')
    else:
        print('Empate')


print(__name__)
if __name__ == '__main__':
    main()
