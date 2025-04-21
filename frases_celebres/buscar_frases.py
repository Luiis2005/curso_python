import csv
 
def cargar_frases(ruta_archivo):
    frases = []
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezado si existe
        for fila in lector:
            frases.append(fila)
    return frases
 
def buscar_frases(frases, palabras_clave):
    resultados = []
    for fila in frases:
        frase_completa = ' '.join(fila).lower()
        if all(palabra.lower() in frase_completa for palabra in palabras_clave):
            resultados.append(fila)
    return resultados
 
def main():
    ruta = 'C:/Users/orran/OneDrive/Escritorio/Luis/DesarrolloIV/Curso_python/curso_python/frases_celebres/frases.csv'
    frases = cargar_frases(ruta)
 
    entrada = input("Ingresa una o varias palabras clave para buscar: ")
    palabras_clave = entrada.strip().split()
 
    resultados = buscar_frases(frases, palabras_clave)
 
    if resultados:
        print("\nFrases encontradas:")
        for fila in resultados:
            print(' | '.join(fila))
    else:
        print("No se encontraron frases que coincidan con las palabras clave.")
 
if __name__ == "__main__":
    main()