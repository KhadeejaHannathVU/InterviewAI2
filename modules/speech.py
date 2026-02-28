import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except:
        return ""