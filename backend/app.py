import os
import flask
import google.generativeai as genai
from flask import request, jsonify
from dotenv import load_dotenv

# .envからAPIキーを読み込む
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = flask.Flask(__name__)

@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.get_json()
    keyword = data.get("keyword", "")

    if not keyword:
        return jsonify({"error": "キーワードを入力してください"}), 400

    prompt = f"""
    むかしむかし、{keyword}にまつわる奇妙な昔話がありました。
    ある日、{keyword}にとんでもない出来事が起こります。
    物語をカオスな展開で語ってください。
    """

    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        story = response.text.strip()
        return jsonify({"story": story})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
