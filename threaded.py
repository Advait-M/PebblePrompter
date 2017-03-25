import threading
import time
import os, io
from google.cloud import speech
from oauth2client.client import GoogleCredentials
import pyaudio
import wave
import threading
import pyredb
    
 

#song = AudioSegment.from_wav("file.wav")
#song.export("testme.flac",format = "flac")
# credentials = GoogleCredentials.get_application_default()


flag = 0      #shared between Thread_A and Thread_B
val = 0
val2 = 0
final = ""
class Thread_A(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        
        global flag
        global val     #made global here
        global val2
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1024
        RECORD_SECONDS = 3
        while True:                
                if val%2 == 0:
                    WAVE_OUTPUT_FILENAME = "file1.raw"
                else:
                    WAVE_OUTPUT_FILENAME = "file2.raw"
                
                audio = pyaudio.PyAudio()
                
                # start Recording
                stream = audio.open(format=FORMAT, channels=CHANNELS,
                                rate=RATE, input=True,
                                frames_per_buffer=CHUNK)
                frames = []
                 
                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK)
                    frames.append(data)
         
         
                # stop Recording
                stream.stop_stream()
                stream.close()
                audio.terminate()
                 
                waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'w')

                waveFile.setnchannels(CHANNELS)
                waveFile.setsampwidth(audio.get_sample_size(FORMAT))
                waveFile.setframerate(RATE)
                waveFile.writeframes(b''.join(frames))
                waveFile.close()
                val += 1
                flag = 1

class Thread_B(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global flag
        global val    #made global here
        global val2
        global final
        client = speech.Client.from_service_account_json(r'Prompt-voice-d17c3c6b865a.json')
        pyredb.ForgetMeNot().start()
        pyredb.ForgetMeNot().getText()
        while True:
            if flag == 1:
                if val%2 == 1:
                    file_name = os.path.join(
                        os.path.dirname(__file__),  'file1.raw')
                else:
                    file_name = os.path.join(
                        os.path.dirname(__file__),  'file2.raw')

                # Loads the audio into memory
                with io.open(file_name, 'rb') as audio_file:
                    content = audio_file.read()
                    audio_sample = client.sample(
                        content,
                        source_uri=None,
                        encoding='LINEAR16',
                        sample_rate=16000)

                #print("one")

                # Detects speech in the audio file
                try:
                    alternatives = client.speech_api.sync_recognize(audio_sample)
                    for alternative in alternatives:
                        print('Transcript: {}'.format(alternative.transcript))
                        final += " " + alternative.transcript
                except ValueError:
                    print("RIP WORDS")
                #print("two")
                val2 += 1
                flag = 0
                
                print(final)

a = Thread_A("myThread_name_A")
b = Thread_B("myThread_name_B")

a.start()
b.start()

a.join()
b.join()
