
"""
Ejemplo de como usar la api de 
OpenAI para crear un modelo de 
generador de imagenes (Dall-E)
"""

# Librerias

import shutil
import requests
from ChatGPT import *

# Obteniendo el prompt a partir de la repuesta del modelo CHATGPT

prompt_imagen = respuesta["choices"][0]["message"]["content"]

# Crear imagen

imagen = openai.Image.create(
	prompt = prompt_imagen,
	n = 1,
	size = "1024x1024"
)

# Url de la imagen

image_url = imagen["data"][0]["url"]

# Obtener la url

foto = requests.get(image_url, stream = True)
print("Imagen:", foto)

# Guardando imagen

if foto.status_code == 200:
  with open("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/IMAI/foto_generada.jpg", "wb") as f:
    shutil.copyfileobj(foto.raw, f)
    print("¡Se guardo!")

else:
  print("Error al acceder a la imagen")