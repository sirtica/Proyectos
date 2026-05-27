import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


@app.route("/")
def home():
    return "Servidor funcionando"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON"
        }), 400

    user_message = data.get("message", "")

    try:

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_message
    )

    return jsonify({
        "reply": response.text
    })

except Exception as e:

    return jsonify({
        "error": str(e)
    }), 500


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    app.run(
        host="0.0.0.0",
        port=port
    )
