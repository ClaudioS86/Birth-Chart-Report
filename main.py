
from flask import Flask, request, jsonify
import openai
import os

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
    You are a professional astrology analyst and transformational life coach.

    Generate a detailed and insightful 35-page astrology Birth Chart Report for the following person:

    Name: {name}
    Date of Birth: {birth_date}
    Time of Birth: {birth_time}
    Place of Birth: {birth_place}
    Current Location: {current_location}

    The report must be complete, flowing, and engaging — written with a warm yet informative tone. Avoid technical jargon without explanation. Be sure to include:

    ✅ An introduction explaining the purpose and power of astrology
    ✅ Full interpretations of the following:

    - Sun, Moon, and Rising Sign
    - All personal planets (Mercury, Venus, Mars)
    - Social planets (Jupiter, Saturn)
    - Transpersonal planets (Uranus, Neptune, Pluto)
    - All 12 Houses (with planet positions and meanings)
    - Major aspects between planets (conjunction, square, trine, opposition, sextile, etc.)
    - Key astrological configurations (e.g., Stelliums, Grand Trines, T-squares, etc.)
    - North Node, South Node, and karmic influences
    - Chiron and other relevant asteroids (optional)
    - Practical life guidance for each section (career, love, growth)

    Structure the report with well-formatted sections and natural transitions. The language should be inspiring, personalized, and written as if by a seasoned astrology coach working with a real client.

    Do not write a letter. This is a full-length reading. The tone should feel deep, wise, yet accessible.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert astrologer who writes insightful and inspiring birth chart readings for clients."
            },
            {
                "role": "user",
                "content": prompt
            }
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

    system_prompt = "You are a Human Design Analyst and Coach. You generate deep, structured reports to help people understand their energetic blueprint."

    prompt = f"""
Generate a detailed Human Design Report of at least 70 pages for {name}, born on {birth_date} at {birth_time} in {birth_place}, currently in {current_location}.

✅ Include:
- Description of all 9 centers (defined and undefined), one by one
- Activated channels and how they interact
- Open/closed gates with detailed meanings
- Deep analysis of the Incarnation Cross with all 4 gates
- Interpretation of the combined profile lines (contextual and evolutionary)
- Optional: transit energy (if relevant)
- Interpersonal dynamics based on open centers
- Potential external conditioning + shadow work
- Daily life coaching advice with examples

The style must be professional and explanatory, as if written by a certified Human Design Coach. Avoid letter format. Use Markdown-style structure with titles, subheadings, and bullet points. Be clear, precise, and helpful.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
