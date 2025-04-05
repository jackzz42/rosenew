import speech_recognition as sr
from TTS.api import TTS
from emotion_net import predict_emotion

# Initialize Coqui TTS (pretrained)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def speak(text, emotion="friendly"):
    style_map = {
        "romantic": 0.4,
        "friendly": 0.8,
        "angry": 1.5,
        "caring": 0.5
    }
    speed = style_map.get(emotion, 1.0)
    tts.tts_to_file(text=text, file_path="output.wav", speaker_wav=None, speed=speed)
    
    import playsound
    playsound.playsound("output.wav")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Sorry, I couldn't understand that."

def speak_emotionally(text):
    mood = predict_emotion(text)
    speak(text, mood)
