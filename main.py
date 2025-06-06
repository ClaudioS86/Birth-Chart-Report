
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-birth-section-1", methods=["POST"])
def generate_birth_section_1():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a professional astrology analyst and coach, write the first section of a 35-page Birth Chart Report. Focus on foundational elements: the role and meaning of astrology, Sun, Moon, and Rising Sign, the 12 zodiac signs, the four elements (Fire, Earth, Air, Water), and modalities (Cardinal, Fixed, Mutable).

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-birth-section-2", methods=["POST"])
def generate_birth_section_2():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a professional astrology analyst and coach, write the second section of a 35-page Birth Chart Report. Analyze all planets (personal, social, transpersonal), all 12 astrological Houses, planetary placements within the Houses, and major aspects (conjunction, opposition, square, trine, sextile, etc.).

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-birth-section-3", methods=["POST"])
def generate_birth_section_3():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a professional astrology analyst and coach, write the third section of a 35-page Birth Chart Report. Explore karmic elements: North Node, South Node, Chiron, asteroid influences (optional), significant configurations (stelliums, Yods, etc.), and life guidance for personal growth.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-1", methods=["POST"])
def generate_human_design_section_1():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section one of a 70-page report. Focus on Type, Strategy, Authority, Profile, Definition, and Incarnation Cross (with interpretation of all 4 gates).

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-2", methods=["POST"])
def generate_human_design_section_2():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section two of a 70-page report. Analyze all 9 Centers in detail: identify which are defined/undefined and explain their function and role.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-3", methods=["POST"])
def generate_human_design_section_3():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section three of a 70-page report. Analyze all activated Channels, how they interact, and how their combined energy influences the person’s design.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-4", methods=["POST"])
def generate_human_design_section_4():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section four of a 70-page report. Explain all open/closed Gates, their meanings, and implications on daily behavior and perception.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-5", methods=["POST"])
def generate_human_design_section_5():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section five of a 70-page report. Provide an in-depth analysis of the Profile lines, including evolutionary development and karmic themes.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-6", methods=["POST"])
def generate_human_design_section_6():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section six of a 70-page report. Explore conditioning patterns via open Centers and offer suggested Shadow Work practices.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})

@app.route("/generate-human-design-section-7", methods=["POST"])
def generate_human_design_section_7():
    data = request.get_json()
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    current_location = data.get("current_location")

    prompt = f"""As a Human Design Analyst and Coach, write section seven of a 70-page report. Provide practical alignment strategies, daily routines, and coaching suggestions for living in alignment with the person’s design.

Name: {name}
Date of Birth: {birth_date}
Time of Birth: {birth_time}
Place of Birth: {birth_place}
Current Location: {current_location}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": "You are an expert astrologer and Human Design analyst who writes insightful, complete and inspiring reports for clients." },
            { "role": "user", "content": prompt }
        ]
    )

    report_text = response["choices"][0]["message"]["content"]
    return jsonify({"report": report_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
