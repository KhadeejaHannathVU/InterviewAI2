import pyttsx3
import threading
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except:
            return None

    except:
        return None