from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace with your Gemini API key
GEMINI_API_KEY = "AIzaSyCLYBf6FTWSww6t3btziE9rNERZyyY4ink"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please type a message."})

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "prompt": user_message,
        "temperature": 0.7,
        "candidate_count": 1
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        # Debug log
        print("Gemini result:", result)

        reply = result.get("candidates", [{}])[0].get("content", [{}])[0].get("text", "Sorry, no response.")
    except Exception as e:
        print("Error:", e)
        reply = "❌ Unable to connect to Gemini AI."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
