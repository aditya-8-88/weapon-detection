import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from googletrans import Translator

# Load the audio file and increase the volume
audio_file = "1.wav"
audio = AudioSegment.from_wav(audio_file)

# Increase the volume by 10 dB
louder_audio = audio + 10

# Play the enhanced audio
play(louder_audio)

# Convert the enhanced audio to text
recognizer = sr.Recognizer()
with sr.AudioFile("louder_audio.wav") as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language='en')
    print("Recognized Text:", text)

# Translate the recognized text to English
translator = Translator(service_urls=['translate.google.com'])
translation = translator.translate(text, dest='en')
translated_text = translation.text
print("Translated Text:", translated_text)
