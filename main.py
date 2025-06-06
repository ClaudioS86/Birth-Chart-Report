from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-human-design", methods=["POST"])
def generate_human_design_report():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""
You are an expert Human Design analyst and coach. Based on the following birth data:

- Name: {name}
- Birth Date: {birth_date}
- Birth Time: {birth_time}
- Birth Location: {birth_place}
- Current Location: {current_location}

Generate a full Human Design report (at least 70 pages of content). Even if you don’t have access to exact chart software, simulate a complete report by making reasonable assumptions based on standard Human Design logic.

Include these sections in detail:

1. Introduction to Human Design
2. Overview of the client’s chart (assume realistic values)
3. Type – explanation + simulated Type
4. Strategy – explanation + simulated Strategy
5. Authority – explanation + simulated Authority
6. Profile – explanation + simulated Profile (e.g. 4/6, 5/1)
7. Defined vs Open Centers – explain & simulate
8. Not-Self Themes – what to watch out for
9. Strengths & Challenges
10. Career Alignment (based on design)
11. Love & Relationships insights
12. Life Path & Incarnation Cross (simulated)
13. Personalized Recommendations & Action Steps

Write in a flowing, elegant tone as if it were a premium PDF report for a paying client. Use markdown formatting (e.g. **bold titles**, section breaks, etc.).

Begin the report with the client’s name, birth details, and a short warm introduction.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional Human Design expert who writes long, elegant and inspiring reports for clients."},
                {"role": "user", "content": prompt}
            ]
        )
        report = response.choices[0].message.content
        return jsonify({"report": report})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)