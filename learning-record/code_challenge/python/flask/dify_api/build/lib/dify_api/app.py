from flask import Flask, request, jsonify
import requests

# Replace with your actual API endpoint and API key
base_url = "http://localhost:8088/v1"

# The api_key belongs to a workflow or a chatflow
api_key = "app-h5HAMxK3x0mIcqpNct8Lq2p8"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get('query')
    # print('query=>', query)
    api_url = base_url + "/chat-messages"
    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "user": "Ernest710"
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        print("Success:", response.json())
        return jsonify({"result": response.json()})
    else:
        print("Error:", response.status_code, response.text)
        return jsonify({"result": response.status_code}), 201

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     app.run(debug=True)