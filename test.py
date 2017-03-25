import time, io
from google.cloud import speech
client = speech.Client.from_service_account_json(r'C:\Users\Leon\PycharmProjects\Wearhacks2\Prompt-voice-d17c3c6b865a.json')
with io.open("audio.raw", 'rb') as audio_file:
    content = audio_file.read()
sample = client.sample(content=content,
                       encoding=speech.Encoding.LINEAR16,
                       sample_rate=44100)
operation = sample.async_recognize(max_alternatives=2)
retry_count = 100
while retry_count > 0 and not operation.complete:
    retry_count -= 1
    time.sleep(10)
    operation.poll()  # API call
print(operation.complete)

for result in operation.results:
    for alternative in result.alternatives:
        print('=' * 20)
        print(alternative.transcript)
        print(alternative.confidence)