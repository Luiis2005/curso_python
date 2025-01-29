import matplotlib.pyplot as plt
def calcular_y(x:float,m:float,b:float)->float:

    return m*x+b

def test_linea():
    y = calcular_y(0.0,2.0,3.0)
    return y 
def grafica_linea(X:list, Y:list, m:float, b:float):
    plt.plot(X,Y)
    plt.title(f'Linea recta co pendiente={m} e inteseccion en y={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    





if __name__ == "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    if y ==2:

        print("prueba exitosa")
    else:
        print("Prueba fallida")