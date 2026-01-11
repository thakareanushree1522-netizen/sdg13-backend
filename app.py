from flask import Flask, request, jsonify
from flask_cors import CORS  #  Add this

app = Flask(__name__)
CORS(app)  #  Enable CORS for all routes

@app.route("/")
def home():
    return {
        "status": "running",
        "message": "SDG 13 Climate Action Backend Live "
    }

@app.route("/carbon", methods=["POST"])
def carbon():
    data = request.json
    score = sum(data.values())

    if score <= 4:
        level = "Low"
    elif score <= 8:
        level = "Moderate"
    else:
        level = "High"

    return jsonify({
        "carbon_score": score,
        "impact_level": level
    })

if __name__ == "__main__":
    app.run()


