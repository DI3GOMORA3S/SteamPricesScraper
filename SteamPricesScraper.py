import requests
from bs4 import BeautifulSoup

website = "https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/?curator_clanid=1541443"
resultado = requests.get(website)
content = resultado.text

print(content)


import requests
from bs4 import BeautifulSoup

# URL de la página web
url = 'https://example.com'

# Realizar la solicitud HTTP a la página web
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar el div con la clase específica (por ejemplo, "mi-clase")
    div_content = soup.find('div', class_='mi-clase')
    
    # Si se encuentra el div, imprimir su contenido
    if div_content:
        print(div_content.text)
    else:
        print('No se encontró el div con la clase especificada.')
else:
    print(f"Error al acceder a la página: {response.status_code}")