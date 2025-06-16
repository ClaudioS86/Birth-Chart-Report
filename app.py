from flask import Flask, request, jsonify, send_file
from astrolog_utils import run_astrolog_aspects, generate_chart_image
from swisseph_utils import calculate_birth_chart
import os  # <-- IMPORTANTE per leggere la porta da Railway

app = Flask(__name__)

@app.route('/birth-chart', methods=['POST'])
def birth_chart():
    try:
        data = request.get_json()

        birth_date = data["birth_date"]
        birth_time = data["birth_time"]
        lat = data["lat"]
        lon = data["lon"]
        timezone = float(data.get("timezone", 0)) / 3600

        result = calculate_birth_chart(
            birth_date,
            birth_time,
            lat,
            lon,
            timezone
        )

        return jsonify(result), 200

    except Exception as e:
        traceback.print_exc()  # <-- aggiungi questa riga
        return jsonify({"error": str(e)}), 500
        
@app.route("/aspects", methods=["POST"])
def get_aspects():
    data = request.json
    aspects = run_astrolog_aspects(
        birth_date=data["birth_date"],
        birth_time=data["birth_time"],
        latitude=data["lat"],
        longitude=data["lon"],
        timezone=float(data.get("timezone", 0)) / 3600  # Assicura conversione corretta
    )
    return jsonify({"sun_aspects": aspects})

@app.route("/chart-image", methods=["POST"])
def get_chart_image():
    data = request.json
    image_path = generate_chart_image(
        birth_date=data["birth_date"],
        birth_time=data["birth_time"],
        latitude=data["lat"],
        longitude=data["lon"],
        timezone=float(data.get("timezone", 0)) / 3600
    )
    return send_file(image_path, mimetype='image/png')
         
# ✅ QUESTA PARTE È FONDAMENTALE PER RAILWAY
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
