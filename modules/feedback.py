def generate_feedback(posture_score, stress_level):

    try:
        posture_score = int(posture_score)
    except:
        posture_score = 0

    feedback = f"Posture Score: {posture_score}%\n\n"

    if posture_score > 80:
        feedback += "✔ You maintained good posture.\n"
    else:
        feedback += "⚠ Try to sit straight and maintain eye contact.\n"

    if stress_level == "High":
        feedback += "⚠ You seemed slightly stressed. Practice breathing exercises.\n"
    else:
        feedback += "✔ You handled the interview calmly.\n"

    feedback += "\nKeep practicing to improve your confidence."

    return feedback
