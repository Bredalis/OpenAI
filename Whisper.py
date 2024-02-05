
import openai

# Api del modelo

openai.api_key = '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'

# Transcribir audio

url = 'Frase.mp3'

with open(url, 'rb') as audio:
	transcripcion = openai.audio.transcriptions.create(
		model = 'whisper-1', 
		file = audio
	)
	
transcripcion = transcripcion.text
print('Transcripcion audio-texto: \n\n', transcripcion)

# Traduccion de audio

url = open(url, 'rb')

traduccion = openai.audio.translations.create(
	model = 'whisper-1', 
	file = url
)

traduccion = traduccion.text
url.close()

print('\nTraduccion español-ingles: \n\n', traduccion)