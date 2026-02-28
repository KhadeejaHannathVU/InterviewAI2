import threading

# pyttsx3 and speech_recognition are optional; cloud hosts typically lack audio devices
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    def _speak(text):
        def run():
            engine.say(text)
            engine.runAndWait()
        threading.Thread(target=run, daemon=True).start()
except Exception:
    # fallback no-op
    def _speak(text):
        print("[speak stub]", text)

try:
    import speech_recognition as sr
    has_recognizer = True
except ImportError:
    sr = None
    has_recognizer = False


# expose availability flags to callers
speak = _speak

# determine whether microphone access is possible
audio_available = False
if has_recognizer:
    try:
        with sr.Microphone():
            audio_available = True
    except Exception:
        audio_available = False


def listen():
    """Attempt to capture audio using SpeechRecognition; return None on failure."""
    if not has_recognizer or not audio_available:
        return None

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
        except Exception:
            return None

    except Exception:
        # microphone not available or other error
        return None