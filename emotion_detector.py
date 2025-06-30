from textblob import TextBlob
import random

def get_emotion_reply(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    angry_replies = [
        "I'm really sorry you're experiencing this.",
        "I understand how frustrating this can be. I'm here to support you.",
        "That doesn't sound good. I'll escalate this to a human assistant right away.",
        "It’s okay to feel this way. Let's sort it out together.",
        "I hear your concern. Let me connect you to someone who can assist better."
    ]

    sad_replies = [
        "I'm sorry you're feeling this way. You're not alone.",
        "It’s okay to feel down sometimes. Let me know how I can help.",
        "Sending you positive thoughts. I’m here for you.",
        "I’m here to support you. Tell me more if you'd like.",
        "Please don’t worry, let’s work through this together."
    ]

    neutral_replies = [
        "Got it. How can I assist you today?",
        "Thanks for sharing. Let me help you further.",
        "Alright, I'm here to help. What would you like to do next?",
        "I’m ready to assist. Please tell me what you need.",
        "Let’s move ahead together. What would you like me to help with?"
    ]

    happy_replies = [
        "That’s wonderful to hear! 😊 How else can I assist you?",
        "Awesome! I'm here if you need anything more.",
        "Glad to hear that! Let’s keep the good vibes going.",
        "Thanks for the kind words! How can I make your day even better?",
        "You just made my circuits smile! 😄 Let me know what you need next."
    ]


    if any(word in text_lower for word in ["hate", "angry", "furious", "worst", "frustrated"]):
        return "angry", random.choice(angry_replies)

    if any(word in text_lower for word in ["sad", "depressed", "unhappy", "crying", "upset", "not good"]):
        return "sad", random.choice(sad_replies)

    if any(word in text_lower for word in ["awesome", "great", "love", "amazing", "thank you", "helpful"]):
        return "happy", random.choice(happy_replies)

    if any(word in text_lower for word in ["okay", "fine", "normal", "alright", "ok"]):
        return "neutral", random.choice(neutral_replies)

    # 📊 Fallback: Use polarity score
    if polarity < -0.5:
        return "angry", random.choice(angry_replies)
    elif polarity < 0:
        return "sad", random.choice(sad_replies)
    elif polarity < 0.3:
        return "neutral", random.choice(neutral_replies)
    else:
        return "happy", random.choice(happy_replies)
