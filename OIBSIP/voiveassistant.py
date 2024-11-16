import sounddevice as sd
import numpy as np
import speech_recognition as sr

# Set the sample rate and duration for audio capture
sample_rate = 16000  # samples per second
duration = 5  # seconds

# Initialize the recognizer
recognizer = sr.Recognizer()

def record_audio():
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    return audio

def recognize_audio(audio_data):
    print("Recognizing speech...")
    with sr.AudioData(audio_data, sample_rate, 1) as source:
        try:
            text = recognizer.recognize_google(source)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError:
            print("Sorry, the service is down.")

# Capture and recognize speech
audio_data = record_audio()
recognize_audio(audio_data)
