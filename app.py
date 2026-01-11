from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =====================
# HEALTH CHECK
# =====================
@app.route("/", methods=["GET"])
def home():
    return {
        "status": "running",
        "message": "SDG 13 Climate Action Backend Live ✅"
    }

# =====================
# CHAT ROUTE (AI BOT)
# =====================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    # Simple AI logic (no API needed)
    if "climate" in user_message:
        reply = "Climate change refers to long-term changes in temperature and weather patterns."
    elif "carbon" in user_message:
        reply = "Carbon footprint is the total greenhouse gas emissions caused by human activities."
    elif "reduce" in user_message:
        reply = "You can reduce emissions by using public transport, saving electricity, and eating less meat."
    else:
        reply = "I can help with climate action, carbon footprint, and sustainability 🌱"

    return jsonify({"reply": reply})

# =====================
# CARBON FOOTPRINT
# =====================
@app.route("/carbon", methods=["POST"])
def carbon():
    data = request.json

    transport = data.get("transport", 0)
    electricity = data.get("electricity", 0)
    meat = data.get("meat", 0)

    score = (transport * 0.4) + (electricity * 0.05) + (meat * 1.5)

    if score < 15:
        level = "Low 🌱"
    elif score < 30:
        level = "Moderate ⚡"
    else:
        level = "High 🔥"

    return jsonify({
        "carbon_score": round(score, 1),
        "impact_level": level
    })

if __name__ == "__main__":
    app.run()



