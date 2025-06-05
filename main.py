
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/generate-birth-report", methods=["POST"])
def generate_report():
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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
