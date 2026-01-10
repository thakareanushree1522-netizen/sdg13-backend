import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Gemini API key
GEMINI_API_KEY = "AIzaSyDSradiZ1k3a3Q1cfaQIAt190ppm57nzfo"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

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
    result = response.json()

    reply = (
        result.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "Sorry, I could not generate a response.")
    )

    return jsonify({"reply": reply})

# optional local run
if __name__ == "__main__":
    app.run(debug=True)
