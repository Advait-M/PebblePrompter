import os, io
from google.cloud import speech
from oauth2client.client import GoogleCredentials
import pyaudio
import wave
import threading
    
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.raw"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
#song = AudioSegment.from_wav("file.wav")
#song.export("testme.flac",format = "flac")
# credentials = GoogleCredentials.get_application_default()
client = speech.Client.from_service_account_json(r'Prompt-voice-d17c3c6b865a.json')
file_name = os.path.join(
    os.path.dirname(__file__),  'file.raw')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio_sample = client.sample(
        content,
        source_uri=None,
        encoding='LINEAR16',
        sample_rate=16000)

print("one")

# Detects speech in the audio file
alternatives = client.speech_api.sync_recognize(audio_sample)
print("two")
for alternative in alternatives:
    print('Transcript: {}'.format(alternative.transcript))
