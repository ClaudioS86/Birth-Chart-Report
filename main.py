
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
You are a certified Human Design Analyst and Coach. Based on the following birth information, generate a comprehensive and professional Human Design report in an analytical, objective tone (no letter-style writing). Assume you are producing a premium report for a paying client who expects clarity, technical depth, and real-world guidance.

Client Data:
- Name: {name}
- Birth Date: {birth_date}
- Birth Time: {birth_time}
- Birth Place: {birth_place}
- Current Location: {current_location}

The report must be structured and detailed, covering the following areas in depth:

1. **Human Design Chart Overview** – What a Bodygraph is and what this client's chart looks like (simulate accurate structural logic).

2. **Type & Aura Mechanics** – Simulated Type (e.g., Generator), aura interaction style, core behavioral tendencies.

3. **Strategy & Authority** – Explain the correct way for this Type to make decisions, with realistic simulation of internal mechanics.

4. **Defined vs Undefined/Open Centers** – Analyze all 9 Centers:
   - Root
   - Spleen
   - Solar Plexus
   - Sacral
   - Ego/Heart
   - G-Center
   - Throat
   - Ajna
   - Head
   For each: state whether it's defined/open and describe the energetic implications.

5. **Profile Lines** – Simulate profile (e.g., 5/1) and explain each line's role in the client's life path.

6. **Channels** – Simulate activated channels and explain the function of each channel and how they interact across centers.

7. **Gates** – Simulate open and closed gates, describe their individual meaning and relevance to this client's life theme.

8. **Incarnation Cross** – Simulate an Incarnation Cross and explain all 4 gates that compose it. Describe the life purpose and evolutionary storyline.

9. **Energy of Transits (optional)** – Briefly describe how planetary transits might influence this chart over time.

10. **Relationship Dynamics** – Explain how open centers impact connection with others, where conditioning may arise in close relationships.

11. **Shadow Work & Conditioning** – Identify potential sources of conditioning and distortion. Provide insight into emotional or behavioral patterns to observe and transform.

12. **Coaching Integration & Alignment Practices** – Provide practical tools or exercises for aligning with the design (e.g., body-based decision making, journaling prompts, energetic hygiene, relationship reflection, environment awareness).

Format using clear markdown structure:
- Use **section headers**
- Use bullet points or short paragraphs where needed
- Do NOT write an introduction or conclusion
- Do NOT make the tone emotional, personal or poetic — this is a technical, grounded guide

Keep the entire response long and comprehensive — simulate the equivalent of a 70-page document if exported to PDF.
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
