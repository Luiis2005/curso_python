import requests
from bs4 import BeautifulSoup

def obtener_tipo_cambio():
    # URL de la página a scrapear
    url = 'https://www.eldolar.info/es-MX/mexico/dia/hoy'
    
    # Realizar la solicitud HTTP
    respuesta = requests.get(url)
    
    # Verificar que la solicitud fue exitosa
    if respuesta.status_code != 200:
        raise Exception(f'Error al acceder a la página: {respuesta.status_code}')
    
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    
    # Extraer el tipo de cambio promedio
    tipo_cambio_promedio = soup.find('div', class_='exchange-rate').find('p').text.strip()
    print(f'Tipo de cambio promedio del dólar en México hoy: {tipo_cambio_promedio}')
    
    # Extraer las tasas de compra y venta por banco
    tabla_bancos = soup.find('table', class_='table table-striped table-hover table-bordered')
    filas = tabla_bancos.find_all('tr')[1:]  # Omitir la fila de encabezados
    
    print('\nTasas de compra y venta por banco:')
    for fila in filas:
        columnas = fila.find_all('td')
        banco = columnas[0].text.strip()
        compra = columnas[1].text.strip()
        venta = columnas[2].text.strip()
        print(f'{banco}: Compra - {compra}, Venta - {venta}')

# Ejecutar la función
obtener_tipo_cambio()
