import requests

# Ollama 的 API 端点
API_URL = "http://localhost:11434/api/generate"

# 定义请求的 JSON 数据
data = {
    "model": "deepseek-r1:1.5b",  # 指定要使用的模型，可以根据需要更改
    "prompt": "你好，介绍一下你自己",  # 输入的提示信息
    "stream": False  # 是否启用流式响应，这里设置为 False
}

try:
    # 发送 POST 请求
    response = requests.post(API_URL, json=data)
    # 检查响应状态码
    response.raise_for_status()

    # 解析响应的 JSON 数据
    result = response.json()
    # 提取生成的文本
    generated_text = result.get("response", "")
    print("生成的文本:")
    print(generated_text)
except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except ValueError as e:
    print(f"解析 JSON 数据出错: {e}")