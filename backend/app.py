import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 環境変数からAPIキーを取得
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.get_json()
    print(f"🔍 受け取ったデータ: {data}")  # デバッグ用
    prompt = data.get("prompt", "むかしむかし")

    # Gemini API へリクエストを送信
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to get response from Gemini API", "details": response.json()}), response.status_code

    # Gemini API のレスポンスを取得
    gemini_response = response.json()

    # AIが生成したストーリーを抽出
    try:
        story = gemini_response["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return jsonify({"error": "Unexpected response format", "details": gemini_response}), 500

    return jsonify({"story": story})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
