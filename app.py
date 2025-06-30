from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_reply():
    user_data = request.get_json()
    user_msg = user_data.get('message')
    return jsonify({
        'reply': "I'm not sure how to reply yet 😅",
        'emotion': "neutral"
    })

if __name__ == '__main__':
    app.run(debug=True)

