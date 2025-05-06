from flask import Flask, request, jsonify, render_template
import openai, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    messages = [
        {"role": "system", "content": "Eres un profesor educativo, amable y claro. Responde como si explicaras a un estudiante de nivel secundario."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    return jsonify({"reply": response.choices[0].message["content"]})

if __name__ == "__main__":
    app.run(debug=True)
