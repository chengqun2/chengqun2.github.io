import requests

# Replace with your actual API endpoint and API key
api_url = "http://localhost:8088/v1/chat-messages"

# The api_key belongs to a workflow or a chatflow
api_key = "app-h5HAMxK3x0mIcqpNct8Lq2p8"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "inputs": {},
    "query": "好好学习，天天向上！",
    "response_mode": "blocking",
    "user": "Ernest710"
}

response = requests.post(api_url, headers=headers, json=data)

if response.status_code == 200:
    # for chunk in response.iter_lines():
    #     if chunk:
    #         decoded_chunk = chunk.decode('utf-8')
    #         if decoded_chunk.startswith('data: '):
    #             content = decoded_chunk[6:]
    #             print(content, end='', flush=True)
    print("Success:", response.json())
    # print("total_tokens:", response.json()['total_tokens'])
else:
    print("Error:", response.status_code, response.text)