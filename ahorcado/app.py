
import string
import unicodedata
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla='plantilla'):

    oraciones = fn 

    #cargo las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)

    #cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    #obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5 # 5 oportunidades de fallar
    p = choice(palabras) # elegimos una palabra al azar
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o> 0:
        fn.despliega_plantilla(plantillas, o)
        fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print(f'Felicidades, adivinaste la palabra {p}')
            break

if __name__ == '__main__':
    archivo = './datos/pg15532.txt'
    main(archivo)