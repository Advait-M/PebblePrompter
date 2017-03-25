import speech_recognition as sr
from os import path
AUDIO_FILE_EN = path.join(path.dirname(path.realpath(__file__)), "output.wav")
##AUDIO_FILE_FR = path.join(path.dirname(path.realpath(__file__)), "french.aiff")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE_EN) as source:
    audio_en = r.record(source) # read the entire audio file
##with sr.AudioFile(AUDIO_FILE_FR) as source:
##    audio_fr = r.record(source) # read the entire audio file

# recognize keywords using Sphinx
##try:
##    print("Sphinx recognition for \"one two three\" with different sets of keywords:")
##    print(r.recognize_sphinx(audio_en, keyword_entries=[("one", 1.0), ("two", 1.0), ("three", 1.0)]))
##    print(r.recognize_sphinx(audio_en, keyword_entries=[("wan", 0.95), ("too", 1.0), ("tree", 1.0)]))
##    print(r.recognize_sphinx(audio_en, keyword_entries=[("un", 0.95), ("to", 1.0), ("tee", 1.0)]))
##except sr.UnknownValueError:
##    print("Sphinx could not understand audio")
##except sr.RequestError as e:
##    print("Sphinx error; {0}".format(e))

# recognize preferred phrases using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "prompt-voice",
  "private_key_id": "d17c3c6b865a89b69e02ed75769d6d70bf2b63e2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDDWoKsJOXY11o7\nk1JR9wqxWY7eP16sdLlcp28rBGOZUyjvHOiT1miZEoavvX7teqI1yFno2ciYyzwp\nk88Ad69H9ui8sPu0LZPt5GfA8pKV4z7DNUpytORlT0J+oLMmqwGiWJGwuh6tpOw0\nHVHoHmPXwBhA2v6BEw1Lk0r8stAVJiJaJYI4IPGzhNsJJBqQlFOFsg1sXh8pMfgQ\nhUon5Eq7GR788DaIpOt85Z2dbvNrovc+xS/LzDouji3keTw0fk26uPJEXhHed1sy\nqOFmhn5qIcWsQQYw66DIaebWoT7bcvyibY8ivcmWIWP51+s0osIYY9FKWfz+HJFQ\n+bueF+unAgMBAAECggEBALCYZYAQauc25g7tAoGt/TCNcSVfy8nCSr6DbW9JrG+y\nSVK+o1DhhfS6Vp8PgmpTbceIsh5YoYneTyiWwY3+o6k+fu30X9VlTlDDJTe7EOAG\naXo19nLzK3SZzdaClvDhrbyArFNCLPF0IUKLLrvSnRcwQ7x9O4ybGG21XRhK3Of/\n2CA4WfShMKfpTNDF1RFLKKL3BgAc0kGBg629vpveNiG3TPF8UfogV2oqlFHzCeT1\nq0/dRj+thd+Uchimg4nRJNyrnmRBRQd8MWL8ZpGFEl1fTf68v7WMx1gMyas2/mEK\n10BNNDw2OTlWvJI+GGZ3K2AswqIX++Wu11f6qsC27WECgYEA7JLiqsHeeSHSiIID\nOSAUfuyICyJ3ZnIamp1jHm61bhdQF3U2TpuuKqYhSHZXQUVIrYh0FWmRieh12+tL\n6sxqPQrk5zEKekg5QhrXSH/Zu67pFlg7El+n5FXN8zREsQ+bNSWuR9rWdzHSdDJ+\nj20Ni3Eg1BWZxAFa5bz1eeGrJusCgYEA02UeMHAlB637loh/7+kKRUQ2ZdD3kEtK\nBUj0CX5BvsFaT57HN6GGRtWeFrOinJia06/0HvFUBVfWC1yTx4btnOzORjkyvwJr\nsM1d7EpN0VN9fzvquAVFel2bpoLQhpI6gbsf8rOyM1VkXHEa/BuWT84ZaGi/m+qU\nJ+SfY+SNVzUCgYEAwRN0OOa22me3Or/ZP5MmBxymP2gmyI6RleSjk5/JJQuTy0FX\nTDqUn6wsd8ZVmiigkzhNfXhGVqZJIm5b7Epe3mj4vpLwuTIewQvE7h+iJSIwi5MA\nyxMUpC8/QaFD+roA8xRIs84vwOIBn+HiFs5rAoYWw+DJOQXeGKfqNEnwdHcCgYB5\nuvHefMWmHXcSITpjAbRLXNNiYCofKmvOjUsSKGVdnmQOE2Wu0FHNeneVpQ3P1UTa\n/6i5JMj4ZrM4SbBDppwv0GGcKJXjTlaLMkeSqNsU3loXKX6pR0fSBhN6mDvSMmSE\njigAj5/fVZ38aZlbcdtly03wRNmJxFRagJmUYWlOvQKBgQDl8vEJ464Uwo3BfpZP\n1rdkCT8Oyr1OfCi+GOR9fHAf/gL2tuPKDCWSqlX6G+jFH0sT0Mbcf0dT5UrqbN+g\ndtDwuz0DOe9OLNE3K4EWx0MNo84jx5yjApMx0xH19qm4mu/5Vcmdawdn8i3FD7RC\ng9beXiipyUe7bZecBifLx0s1nA==\n-----END PRIVATE KEY-----\n",
  "client_email": "402924590080-compute@developer.gserviceaccount.com",
  "client_id": "105965002057051309071",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/402924590080-compute%40developer.gserviceaccount.com"
}"""

client = speech.Client.from_service_account_json(r'C:\Users\Leon\PycharmProjects\Wearhacks2\Prompt-voice-d17c3c6b865a.json')

try:
    print("Google Cloud Speech recognition for \"numero\" with different sets of preferred phrases:")
    print(r.recognize_google_cloud(audio_en, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
    print(r.recognize_google_cloud(audio_en, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, preferred_phrases=["noomarow"]))
##    print(r.recognize_google_cloud(audio_en, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
