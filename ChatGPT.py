
"""
ChatGPT: es un modelo
de nlp, que genera 
texto y resumenes
"""

# Librerias

import openai
from textwrap import wrap

# Api del modelo

openai.api_key = "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"

# Crear prompt y la estructura del mensaje

prompt = input("Ingrese su pregunta: ")
mensajes = [
	{"role":"system", "content": "dame una respuesta muy corta"},
	{"role": "user", "content": prompt}
]

# Modelo y respuesta

modelo = "gpt-3.5-turbo"

respuesta = openai.chat.completions.create(
	model = modelo,
	messages = mensajes,
	temperature = 0,
	max_tokens = 1000 
)

print("\n".join(wrap(respuesta.choices[0].message.content)))