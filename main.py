import os
import json
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-birth-report", methods=["POST"])
def generate_birth_report():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""
Generate a complete personalized astrology birth chart reading for the following user:

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}

Format the report in clear, structured, and informative English. Include the meanings of the positions of the Sun, Moon, and planets, as well as houses and aspects.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert astrologer and writer."},
            {"role": "user", "content": prompt}
        ]
    )
    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design", methods=["POST"])
def generate_human_design():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""
Act as a certified Human Design analyst and coach. Generate a complete, in-depth 70-page Human Design report for the following individual:

Name: {name}
Birth Date: {birth_date}
Birth Time: {birth_time}
Birth Place: {birth_place}
Current Location: {current_location}

The report must include:
- Detailed analysis of all 9 centers, defined or undefined
- Explanation of all active channels and how they interact
- Description of open/closed gates with their meaning
- Deep insights on:
  - Incarnation Cross (include all 4 gates involved)
  - Combined Profile lines in evolutionary context
  - Transit energy (optional)
  - Interpersonal dynamics based on open centers
- Potential external conditioning + suggested shadow work
- Coaching section with practical tips and real-world alignment advice

Use a professional tone, clear formatting with headings, and structure the document as a Human Design analyst would do for a paying client.
Do not write a letter. This is a report.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Human Design analyst and coach."},
            {"role": "user", "content": prompt}
        ]
    )
    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)