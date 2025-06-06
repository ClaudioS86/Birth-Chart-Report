
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
    Create a 35-page personalized astrology birth chart report for a person named {name} born on {birth_date} at {birth_time} in {birth_place}, currently located in {current_location}.
    The tone should be clear, warm, and insightful. Use simple but elegant language. Include analysis of Sun, Moon, Ascendant, planetary positions, and houses.
    Provide practical and motivational advice in each section. Format with headings and sections.
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
