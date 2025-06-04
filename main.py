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

    prompt = f"""
Sei un astrologo professionista. Crea un report dettagliato del tema natale per un cliente.
Nome: {name}
Data di nascita: {birth_date}
Ora di nascita: {birth_time}
Luogo di nascita: {birth_place}

Descrivi in modo ispirazionale e profondo la posizione del Sole, Luna, Ascendente, pianeti personali e gli aspetti più rilevanti.
Scrivi circa 3000 parole, divise in sezioni.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sei un esperto astrologo e scrivi in modo evocativo e professionale."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3500,
        temperature=0.7
    )

    report_text = response['choices'][0]['message']['content']
    return jsonify({"report": report_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
