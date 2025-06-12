from flask import Flask, request, jsonify
from swisseph_utils import calculate_birth_chart
import os

app = Flask(__name__)

@app.route("/birth-chart", methods=["POST"])
def birth_chart():
    data = request.get_json()
    result = calculate_birth_chart(
        data["birth_date"],
        data["birth_time"],
        data["lat"],
        data["lon"]
    )
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))