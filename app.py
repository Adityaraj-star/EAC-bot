from flask import Flask, render_template, request, jsonify
from emotion_detector import get_emotion_reply

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_reply():
    data = request.get_json()
    user_msg = data.get('message')

    emotion, reply = get_emotion_reply(user_msg)

    return jsonify({
        'reply': reply,
        'emotion': emotion
    })
    
if __name__ == '__main__':
    app.run(debug=True)

