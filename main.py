import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# API KEY de Gemini desde variables de entorno
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Configurar Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Modelo
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/")
def home():
    return "Servidor funcionando"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "error": "Falta el campo 'message'"
        }), 400

    user_message = data["message"]

    try:

        response = model.generate_content(user_message)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
