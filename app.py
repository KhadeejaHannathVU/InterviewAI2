import streamlit as st
import cv2
import random
import time
from modules.voice import speak, listen, audio_available
from modules.vision import posture_feedback

st.set_page_config(
    page_title="AI Interview System",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview & Posture Trainer")
if not audio_available:
    st.warning("Audio input/output is unavailable in this environment; speech features will be disabled.")
st.markdown("---")

# ---------------- QUESTION BANK ----------------

softskill_questions = [
    "Please introduce yourself.",
    "What are your strengths?",
    "What is your biggest weakness?",
    "How do you handle pressure?",
    "Where do you see yourself in five years?"
]

domain_questions = {
    "Software Developer": [
        "What is object oriented programming?",
        "Explain list and tuple difference.",
        "What is API?",
        "What is version control?"
    ],
    "Digital Marketer": [
        "What is SEO?",
        "Explain social media marketing.",
        "What is conversion rate?"
    ],
    "Electronics Core": [
        "What is a diode?",
        "Explain Ohm's Law.",
        "What is a transistor?"
    ],
    "Electrical Core": [
        "What is power factor?",
        "Difference between AC and DC?",
        "What is transformer?"
    ],
    "Mechanical Core": [
        "What is thermodynamics?",
        "Explain stress and strain.",
        "What is CNC machine?"
    ]
}

# ---------------- SESSION STATE DEFAULTS ----------------

defaults = {
    "mode": None,
    "interview_type": None,
    "domain": None,
    "question_index": 0,
    "interview_running": False,
    "bad_posture_count": 0,
    "total_posture_score": 0,
    "frame_count": 0,
    "filler_count": 0,
    "valid_answers": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("⚙️ Controls")

    st.session_state.mode = st.radio(
        "Select Mode",
        ["Practice", "Interview"]
    )

    camera_on = st.toggle("📷 Camera ON/OFF")

    if st.session_state.mode == "Interview":

        st.session_state.interview_type = st.radio(
            "Interview Type",
            ["Soft Skills", "Domain Based"]
        )

        if st.session_state.interview_type == "Domain Based":
            st.session_state.domain = st.selectbox(
                "Select Domain",
                list(domain_questions.keys())
            )

        if st.button("🚀 Start Interview"):
            st.session_state.question_index = 0
            st.session_state.interview_running = True
            speak("Welcome to your interview. Let us begin.")

# ---------------- STATUS BAR ----------------

col_status1, col_status2, col_status3 = st.columns(3)

col_status1.metric("Mode", st.session_state.mode)
col_status2.metric("Camera", "ON 🟢" if camera_on else "OFF 🔴")
col_status3.metric("Questions Answered", st.session_state.question_index)

st.markdown("---")

# ---------------- CAMERA DISPLAY ----------------

FRAME_WINDOW = st.image([])

if camera_on:

    camera = cv2.VideoCapture(0)

    while camera_on:

        ret, frame = camera.read()
        if not ret:
            st.error("Camera not accessible")
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame_rgb)

        posture_score = random.randint(60, 95)

        st.session_state.total_posture_score += posture_score
        st.session_state.frame_count += 1

        if posture_score < 75:
            st.session_state.bad_posture_count += 1

        posture_feedback(posture_score)

        # -------- INTERVIEW MODE --------
        if st.session_state.mode == "Interview" and st.session_state.interview_running:

            if st.session_state.interview_type == "Soft Skills":
                questions = softskill_questions
            else:
                questions = domain_questions[st.session_state.domain]

            total_questions = len(questions)

            if st.session_state.question_index < total_questions:

                progress = st.session_state.question_index / total_questions
                st.progress(progress)

                question = questions[st.session_state.question_index]

                st.markdown(f"### 📝 Question {st.session_state.question_index + 1}")
                st.info(question)

                speak(question)
                time.sleep(2)
                speak("You may answer now.")

                answer = listen()

                if answer:
                    filler_words = ["um", "uh", "like", "actually", "basically"]
                    filler_used = sum(answer.count(word) for word in filler_words)

                    st.session_state.filler_count += filler_used
                    st.session_state.valid_answers += 1

                    speak("Thank you for your answer.")
                else:
                    speak("I could not hear clearly. Moving to next question.")

                st.session_state.question_index += 1
                time.sleep(2)

            else:
                avg_posture = (
                    st.session_state.total_posture_score /
                    max(st.session_state.frame_count, 1)
                )

                overall_score = 0

                if avg_posture > 80:
                    posture_feedback_text = "Your posture was confident and professional."
                    overall_score += 3
                else:
                    posture_feedback_text = "You need to improve your posture and maintain eye contact."

                if st.session_state.filler_count < 3:
                    filler_feedback_text = "You spoke clearly with minimal filler words."
                    overall_score += 3
                else:
                    filler_feedback_text = (
                        f"You used {st.session_state.filler_count} filler words. "
                        "Try to reduce words like um or uh."
                    )

                if st.session_state.valid_answers >= 3:
                    overall_score += 4

                st.markdown("## 📊 Performance Report")

                col1, col2, col3 = st.columns(3)
                col1.metric("Avg Posture", round(avg_posture, 1))
                col2.metric("Filler Words", st.session_state.filler_count)
                col3.metric("Score", f"{overall_score}/10")

                st.success(posture_feedback_text)
                st.warning(filler_feedback_text)

                speak("The interview is completed.")
                time.sleep(2)
                speak(posture_feedback_text)
                time.sleep(2)
                speak(filler_feedback_text)
                time.sleep(2)
                speak(f"Your overall score is {overall_score} out of 10.")
                time.sleep(2)
                speak("Keep practicing to improve your confidence.")

                st.session_state.interview_running = False
                break

    camera.release()

else:
    FRAME_WINDOW.empty()