import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# ✅ Replace with your Gemini API key
GEMINI_API_KEY = "AIzaSyAseIFaCJ2nvVs3RP5D4nUPDL8X2cskmmg"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please provide a message."})

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": user_message}]}
        ]
    }

    try:
        # ✅ Make request to Gemini API
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Raise error if status != 200
        result = response.json()

        print("Gemini API result:", result)  # Debug log

        # Extract text from response
        reply = (
            result.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "Sorry, I could not generate a response.")
        )

    except requests.exceptions.RequestException as e:
        # Detailed error logging
        print("Error connecting to Gemini:", e)
        if hasattr(e, "response") and e.response is not None:
            print("Response status:", e.response.status_code, e.response.text)
        reply = "❌ Unable to connect to Gemini AI."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    print("Starting SDG 13 AI backend...")
    app.run(debug=True)
