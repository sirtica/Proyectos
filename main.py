import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-pro")


@app.route("/")
def home():
    return "Servidor funcionando"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON received"
        }), 400

    user_message = data.get("message", "")

    response = model.generate_content(user_message)

    return jsonify({
        "reply": response.text
    })


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    app.run(
        host="0.0.0.0",
        port=port
    )
