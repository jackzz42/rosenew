import queue
import sounddevice as sd
import vosk
import json

q = queue.Queue()
model = vosk.Model("vosk-model")  # Folder path
samplerate = 16000

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def is_wake_word():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        print("Rosee is sleeping... Say 'Hey Rosee'")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if "text" in result:
                    text = result["text"].lower()
                    print("You said:", text)
                    if "hey rosee" in text or "hey love" in text:
                        print("Rosee is awake!")
                        return True
