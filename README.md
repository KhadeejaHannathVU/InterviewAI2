# INTERACT-AI: Voice-Based Intelligent Interview Simulator

---

## Project Description

INTERACT-AI is a **voice-based interview simulator** designed to help candidates practice interviews in a realistic and interactive environment. The system:

* Speaks questions in real-time
* Listens to the candidate’s voice responses
* Monitors posture, filler words, and voice cues
* Provides real-time feedback via a dashboard

**Goal:** Improve confidence, posture, and communication skills during interviews.

---

## Tech Stack

* **Frontend/UI:** Streamlit
* **Computer Vision:** OpenCV, Mediapipe
* **Voice Processing:** pyttsx3, SpeechRecognition, Librosa
* **Data Handling & Visualization:** NumPy, Plotly

---

## Features

1. **Voice-Based Interview Questions** – AI asks questions and listens to responses.
2. **Posture Detection** – Monitors if the candidate maintains a proper posture using webcam.
3. **Filler Word & Voice Analysis** – Tracks speech patterns and identifies filler words.
4. **Real-Time Feedback Dashboard** – Displays transcript, posture feedback, and suggestions.
5. **Role & Mode Selection** – Soft skills or domain-specific interview modes.
6. **Interactive Charts** – Visual representation of posture, confidence, and stress metrics.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd InterviewAI
pip install streamlit opencv-python mediapipe pyttsx3 speechrecognition librosa numpy plotly
```

---

## Run Commands

Start the Streamlit app:

```bash
streamlit run app.py
```

* Open your browser at **[http://localhost:8504)**
* Select **mode** and **role**, then click **Start Interview**

---

## Screenshots

> Replace placeholders with your actual screenshots

**Home / Mode Selection**
![Home Screen](<img width="360" height="867" alt="image" src="https://github.com/user-attachments/assets/496fd938-f9f7-4a5e-a4d1-672d8685b0c7" />)
**Dashboard Feedback**
![Dashboard Screen](<img width="1463" height="495" alt="image" src="https://github.com/user-attachments/assets/ff2f700d-757d-430e-8b2f-6e1a80dbf574" />
)

---




**Flow:**
`User → Webcam + Mic → Streamlit → Posture & Voice Analysis → Dashboard Feedback`

---

## API Documentation

Not applicable as this is a **local app** with no separate backend.

---

## Team Members
Krishnapriya s:** AI & Processing Lead – Voice, posture detection, stress analysis
Khadeeja Hannath V U:** UI & Interaction Lead – Streamlit interface, dashboard, session flow
