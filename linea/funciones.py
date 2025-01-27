
def calcular_y(x,m,b):

    return m*x+b

if __name__ == "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    if y ==2:

        print("prueba exitosa")
    else:
        print("Prueba fallida")