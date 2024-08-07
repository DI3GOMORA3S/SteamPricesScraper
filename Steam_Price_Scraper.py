import requests
from bs4 import BeautifulSoup

# URL de la página web
url = 'https://store.steampowered.com/app/2395210/Tony_Hawks_Pro_Skater_1__2/'

# Realizar la solicitud HTTP a la página web
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar el div con la clase específica (por ejemplo, "mi-clase")
    div_content = soup.find('div', class_='discount_original_price')
    
    # Si se encuentra el div, imprimir su contenido
    if div_content:
        print(div_content.text)
    else:
        print('No se encontró el div con la clase especificada.')
else:
    print(f"Error al acceder a la página: {response.status_code}")