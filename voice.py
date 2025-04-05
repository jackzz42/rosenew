import sounddevice as sd
import soundfile as sf
import torch
from TTS.api import TTS
import speech_recognition as sr

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=torch.cuda.is_available())

def speak(text):
    tts.tts_to_file(text=text, file_path="output.wav")
    data, fs = sf.read("output.wav")
    sd.play(data, fs)
    sd.wait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return "Sorry, I couldn't understand that."
