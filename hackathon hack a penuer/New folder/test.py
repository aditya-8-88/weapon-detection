from google.cloud import speech
from google.cloud import translate_v2 as translate

# Set the path to your audio file
audio_file_path = "output_audio_file.wav"

# Create a Speech-to-Text client
client = speech.SpeechClient()

# Read the audio file
with open(audio_file_path, "rb") as audio_file:
    audio_data = audio_file.read()

# Configure the audio settings
audio = speech.RecognitionAudio(content=audio_data)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="hi-IN",  # Set the language code for Hindi
)

# Perform the speech recognition
response = client.recognize(config=config, audio=audio)

# Process the response
captions = ""
for result in response.results:
    captions += result.alternatives[0].transcript + " "

# Translate the Hindi captions to English
translator = translate.Client()
translated_captions = translator.translate(captions, source_language='hi', target_language='en')['translatedText']

# Print the generated English captions
print(translated_captions)
