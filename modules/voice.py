"""Simple audio helper with fallbacks for cloud environments."""

import threading

# attempt to initialise pyttsx3; fall back to no-op if it fails (e.g. no espeak)
try:
    import pyttsx3
    _engine = None
    try:
        _engine = pyttsx3.init()
        _engine.setProperty('rate', 170)
    except Exception:
        _engine = None
except ImportError:
    _engine = None


def _speak(text: str) -> None:
    if _engine:
        def run():
            _engine.say(text)
            _engine.runAndWait()
        threading.Thread(target=run, daemon=True).start()
    else:
        # silent fallback; useful when audio unavailable on server
        print("[speak disabled]", text)

# speech recognition may not be available or usable
try:
    import speech_recognition as sr
    has_recognizer = True
except ImportError:
    sr = None
    has_recognizer = False

# detect whether microphone access works
audio_available = False
if has_recognizer:
    try:
        with sr.Microphone():
            audio_available = True
    except Exception:
        audio_available = False

speak = _speak

def listen():
    """Attempt to capture audio; return None if impossible."""
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
            return recognizer.recognize_google(audio).lower()
        except Exception:
            return None
    except Exception:
        return None
