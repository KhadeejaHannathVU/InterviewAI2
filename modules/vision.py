from modules.voice import speak
import time

last_feedback = None
last_spoken_time = 0

def posture_feedback(posture_score):

    global last_feedback, last_spoken_time
    current_time = time.time()

    if current_time - last_spoken_time < 5:
        return

    if posture_score > 80:
        if last_feedback != "good":
            speak("Great posture. Keep it up.")
            last_feedback = "good"
            last_spoken_time = current_time
    else:
        if last_feedback != "bad":
            speak("Please sit straight and maintain eye contact.")
            last_feedback = "bad"
            last_spoken_time = current_time