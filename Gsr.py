import os, io
from google.cloud import speech
from oauth2client.client import GoogleCredentials

# credentials = GoogleCredentials.get_application_default()
client = speech.Client.from_service_account_json(r'C:\Users\Leon\PycharmProjects\Wearhacks2\Prompt-voice-d17c3c6b865a.json')
file_name = os.path.join(
    os.path.dirname(__file__),  'audio.raw')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio_sample = client.sample(
        content,
        source_uri=None,
        encoding='LINEAR16',
        sample_rate=16000)



# Detects speech in the audio file
alternatives = client.speech_api.sync_recognize(audio_sample)

for alternative in alternatives:
    print('Transcript: {}'.format(alternative.transcript))