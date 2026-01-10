from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please type a message."})

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-1.5-flash:generateContent"
        f"?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_message}]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
        result = response.json()

        reply = result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("Gemini error:", e)
        reply = "❌ Gemini AI is not responding."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

