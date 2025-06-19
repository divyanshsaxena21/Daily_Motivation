from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv
from tavily_helper import get_inspirational_article

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate_motivation():
    data = request.get_json()
    mood = data.get("mood", "")

    if not mood:
        return jsonify({"error": "Mood is required"}), 400

    prompt = f"""
You are a motivational coach. A user is feeling "{mood}". Provide:
1. A short, uplifting message (1–2 sentences),
2. A powerful quote (real or fictional),
3. A simple tip or action step they can do now.

Return your response in this format:
Message: ...
Quote: ...
Tip: ...
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        message = response.choices[0].message.content.strip()

        article_url = get_inspirational_article(f"motivational article about {mood}")
        if article_url:
            message += f"\n\n✨ Bonus Inspiration: {article_url}"

        return jsonify({"result": message})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong generating the response."}), 500


if __name__ == "__main__":
    app.run(debug=True)
