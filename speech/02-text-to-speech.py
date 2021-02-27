import os
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from dotenv import load_dotenv

load_dotenv()

speech_key, service_region = os.getenv('SPEECH_RESOURCE_KEY'), "westus"

speech_config = SpeechConfig(subscription=speech_key, region=service_region)

print("Enter your choice :")
print("1. Output from speaker")
print("2. Save output to a file\n")
choice = int(input())


if(choice == 1):
    audio_config = AudioOutputConfig(use_default_speaker=True)

elif(choice == 2):
    audio_config = AudioOutputConfig(filename=("tts_output/" + input("Enter the name of the output file : ") + ".wav"))


synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async(input("Enter a string : ")) 