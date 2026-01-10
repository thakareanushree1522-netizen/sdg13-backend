import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyDSradiZ1k3a3Q1cfaQIAt190ppm57nzfo"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={AIzaSyDSradiZ1k3a3Q1cfaQIAt190ppm57nzfo}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    reply = (
        data.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "No response")
    )

    return jsonify({"reply": reply})
