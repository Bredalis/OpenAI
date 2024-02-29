
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