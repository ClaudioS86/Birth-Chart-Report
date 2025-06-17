from flask import Flask, request, jsonify, send_file
from get_aspects import run_aspect_calc  # già incluso se hai il file
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

@app.route('/aspects', methods=['POST'])
def aspects():
    try:
        data = request.get_json()
        birth_date = data["birth_date"]
        birth_time = data["birth_time"]
        lat = data["lat"]
        lon = data["lon"]
        timezone = float(data.get("timezone", 0))

        result = run_aspect_calc(
            birth_date,
            birth_time,
            lat,
            lon,
            timezone
        )

        return jsonify(result), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
         
# ✅ QUESTA PARTE È FONDAMENTALE PER RAILWAY
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
