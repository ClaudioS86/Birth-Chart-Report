
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/generate-birth-report", methods=["POST"])
def generate_birth_report():
    data = request.json
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""
You are a professional Western astrologer. Based on the following birth data, write a personalized, detailed and engaging 35-page Birth Chart report in English:

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}

The report should include:
- A structured introduction
- Analysis of the Sun, Moon, and Ascendant signs
- Positions and interpretations of all personal planets
- Analysis of astrological houses and aspects
- Emotional, psychological, and life patterns
- Challenges, strengths, and recurring life themes

Use a professional tone, write in fluent English, and avoid bullet points. Structure the report in paragraphs with headings.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional astrologer writing in English."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3500,
        temperature=0.7
    )

    report_text = response['choices'][0]['message']['content']
    return jsonify({"report": report_text})


@app.route("/generate-human-design", methods=["POST"])
def generate_human_design():
    data = request.json
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""
You are an expert in Human Design analysis. Based on the following birth data, write a detailed, personalized, 70-page Human Design report in English for the client.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}

The report should include:
- Introduction to Human Design
- Detailed explanation of Type, Strategy, Authority, Profile
- Centers (defined and undefined)
- Gates and Channels
- Incarnation Cross
- Strengths and shadows
- Life challenges and energetic dynamics
- Actionable advice and guidance

Write in a professional, empathic, engaging tone. Structure clearly with sections and paragraphs. No bullet points.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional Human Design analyst writing in English."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3500,
        temperature=0.75
    )

    report_text = response['choices'][0]['message']['content']
    return jsonify({"report": report_text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
