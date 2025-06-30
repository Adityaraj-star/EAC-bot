from flask import Flask, render_template, request, jsonify
from emotion_detector import get_emotion_reply
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_reply():
    data = request.get_json()
    user_msg = data.get('message')
    lang = data.get('lang', 'en')

    try:
        translated_msg = GoogleTranslator(source=lang, target='en').translate(user_msg)

        emotion, reply_en = get_emotion_reply(translated_msg)

        final_reply = GoogleTranslator(source='en', target=lang).translate(reply_en)

        with open("chat_logs.txt", "a", encoding="utf-8") as file:
            file.write(f"User ({lang}): {user_msg}\n")
            file.write(f"Translated: {translated_msg}\n")
            file.write(f"Emotion: {emotion}\n")
            file.write(f"Bot: {final_reply}\n")
            file.write("-" * 40 + "\n")

        return jsonify({
            'reply': final_reply,
            'emotion': emotion
        })
    

    except Exception as e:
        return jsonify({
            'reply': "❌ Sorry, something went wrong with translation.",
            'emotion': "neutral"
        })
    
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


