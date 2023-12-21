
"""
Whisper: es un modelo
de nlp para audio
"""

# Libreria

import openai

# Api del modelo
openai.api_key = "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"

# Transcribir audio
url = "C:/Users/Angelica Gerrero/Videos/Audio_Sarcastico.wav"

with open(url, "rb") as audio:
	transcripcion = openai.audio.transcriptions.create(
		model = "whisper-1", 
		file = audio
	)
	
transcripcion = transcripcion.text
print("Transcripcion audio-texto: \n\n", transcripcion)

# Traduccion de audio
url = open(url, "rb")

traduccion = openai.audio.translations.create(
	model = "whisper-1", 
	file = url
)

traduccion = traduccion.text
url.close()

print("\nTraduccion español-ingles: \n\n", traduccion)