import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from database import init_db, get_db
from advisory import get_advisory
from services.weather_service import get_weather
from services.mandi_service import get_prices

load_dotenv()
app = Flask(__name__)
CORS(app)
init_db()

def error(message, status=400):
    return jsonify({"error": message}), status

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "project": "Multilingual Agritech & Resource Advisory Assistant"})

@app.post("/api/farmers")
def create_farmer():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    state = str(data.get("state", "")).strip()
    district = str(data.get("district", "")).strip()
    language = str(data.get("language", "en")).strip()
    if not all([name, state, district]):
        return error("Name, state and district are required.")
    if language not in ("en", "ta", "hi"):
        return error("Language must be en, ta or hi.")
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO farmers(name,state,district,language) VALUES(?,?,?,?)",
            (name, state, district, language)
        )
        farmer_id = cursor.lastrowid
        row = db.execute("SELECT * FROM farmers WHERE id=?", (farmer_id,)).fetchone()
    return jsonify(dict(row)), 201

@app.get("/api/farmers/<int:farmer_id>")
def get_farmer(farmer_id):
    with get_db() as db:
        row = db.execute("SELECT * FROM farmers WHERE id=?", (farmer_id,)).fetchone()
    if row is None:
        return error("Farmer not found.", 404)
    return jsonify(dict(row))

@app.post("/api/advisory")
def advisory():
    data = request.get_json(silent=True) or {}
    crop = str(data.get("crop", "")).strip()
    question = str(data.get("question", "")).strip()
    language = str(data.get("language", "en")).strip()
    if not crop:
        return error("Please enter a crop name.")
    if language not in ("en", "ta", "hi"):
        language = "en"
    return jsonify(get_advisory(crop, question, language))

@app.get("/api/weather")
def weather():
    return jsonify(get_weather(request.args.get("district", "")))

@app.get("/api/mandi")
def mandi():
    return jsonify(get_prices(request.args.get("commodity", ""), request.args.get("district", "")))

@app.post("/api/soil-advice")
def soil_advice():
    data = request.get_json(silent=True) or {}
    try:
        ph = float(data.get("ph"))
    except (TypeError, ValueError):
        return error("Enter a valid soil pH value.")
    if not 0 <= ph <= 14:
        return error("Soil pH must be between 0 and 14.")
    language = data.get("language", "en")
    messages = {
        "en": "This pH value is an initial indicator only. Soil nutrient status and crop suitability require a laboratory soil test and local interpretation.",
        "ta": "இந்த pH மதிப்பு ஆரம்பக் குறியீடு மட்டுமே. மண் ஊட்டச்சத்து மற்றும் பயிர் பொருத்தத்தை அறிய ஆய்வக மண் பரிசோதனையும் உள்ளூர் விளக்கமும் தேவை.",
        "hi": "यह pH मान केवल प्रारंभिक संकेत है। मिट्टी के पोषक तत्व और फसल उपयुक्तता जानने के लिए प्रयोगशाला जाँच और स्थानीय व्याख्या आवश्यक है।"
    }
    return jsonify({"ph": ph, "message": messages.get(language, messages["en"]), "source": "User-entered soil test value; interpretation is general"})

@app.post("/api/feedback")
def feedback():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return error("Feedback message is required.")
    farmer_id = data.get("farmer_id")
    rating = data.get("rating")
    if rating is not None:
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                return error("Rating must be from 1 to 5.")
        except (TypeError, ValueError):
            return error("Rating must be a number from 1 to 5.")
    with get_db() as db:
        db.execute("INSERT INTO feedback(farmer_id,message,rating) VALUES(?,?,?)",
                   (farmer_id, message, rating))
    return jsonify({"message": "Thank you for your feedback."}), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=os.getenv("FLASK_DEBUG", "true").lower() == "true")
