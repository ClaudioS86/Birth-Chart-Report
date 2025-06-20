from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/generate-chart', methods=['POST'])
def generate_chart():
    data = request.json
    date = data.get("date")      # formato: DD/MM/YYYY
    time = data.get("time")      # formato: HH:MM
    location = data.get("location")  # stringa es. "Rome, Italy"
    lat = data.get("lat")
    lon = data.get("lon")
    tz = data.get("timezone")    # es: +2.0

    # Comando shell
    output_path = "chart.png"
    cmd = ["./generate_chart.sh", date, time, str(lat), str(lon), str(tz), location, output_path]
    subprocess.run(cmd, check=True)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
