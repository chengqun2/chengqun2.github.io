# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-e663cfaba4e54d2a84e2ae584d390df4", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "1=1等于几?"},
    ],
    stream=False
)

print(response.choices[0].message.content)