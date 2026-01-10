import requests
from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

GEMINI_API_KEY = "AIzaSyDSradiZ1k3a3Q1cfaQIAt190ppm57nzfo"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

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

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()

        reply = (
            result.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "Sorry, I could not generate a response.")
        )

    except Exception as e:
        print("Error:", e)
        reply = "❌ Unable to connect to Gemini AI."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

