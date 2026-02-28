def analyze_stress(answer_text):

    stress_keywords = ["nervous", "stress", "afraid", "confused", "anxious"]

    for word in stress_keywords:
        if word in answer_text:
            return "High"

    return "Normal"