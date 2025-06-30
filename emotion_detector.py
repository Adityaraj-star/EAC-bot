
from textblob import TextBlob

def get_emotion_reply(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity < -0.5:
        return "angry", "I'm sorry you're upset. Let's connect you to support."
    elif polarity < 0:
        return "sad", "I'm here for you. Can I help with something?"
    elif polarity < 0.3:
        return "neutral", "Thanks for your message. How can I assist?"
    else:
        return "happy", "That's great to hear! 😊 What can I help with?"
