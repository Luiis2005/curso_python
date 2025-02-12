

import string
import unicodedata
from random import choice 
def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r',encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:dict)->dict:
    """
    Función que carga las plantillas del archivo plantillas.json
    """
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    """
    Función que despliega la plantilla de acuerdo al nivel
    """
    if nivel in diccionario:
        template =diccionario[nivel]
        for renglon in template:
            print(renglon)
def obten_palabras(textote:str)->list:
    """
    Función que obtiene las palabras de un texto
    """
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)

    set_palabras = {palabras.strip(string.punctuation) for palabra in set_palabras}
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}

    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)
    
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    # convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    # removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # removemos números, paréntesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)    

def adivina_letra(abc:dict, palaabra:str, letras_adivinadas:set, turnos:int):
    '''
    Adivina una letra de una palabra
    '''
    palabra_oculta = "" 
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f'Tienes {turnos} oportunidades de fallar')
    print(f'El abecedario es: {abc}')
    print(f'La palabra es: {palabra_oculta}')
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print('Ya ingresaste esa letra')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1 
        
if __name__ == '__main__':
    plantillas = carga_plantillas("plantilla")
    despliega_plantilla(plantillas, 5)
    lista_oraciones = carga_archivo('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = t # oportunidades
    adivina_letra(abcdario, p, adivinadas, t)
    