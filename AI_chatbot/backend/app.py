from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_best_answer, save_knowledge
from database import create_table, insert_default_knowledge

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Create database table on startup
create_table()
insert_default_knowledge()
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    answer = get_best_answer(user_message)

    if answer:
        return jsonify({"reply": answer})
    else:
        return jsonify({
            "reply": "Sorry, I don't have an answer for that yet."
        })

@app.route("/")
def home():
    return "AI Chatbot Backend is Running 🚀"

if __name__ == "__main__":
    app.run(debug=True)
