from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['POST'])
def proxy():
    api_key = request.json.get('api_key')
    url = "https://api.grok.xai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "grok-3",
        "prompt": "Hello, Grok! Can you help me with a test?",
        "max_tokens": 50
    }

    try:
        response = requests.post(url, headers=headers, json=data, verify=True)
        return jsonify({"status": response.status_code, "response": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)