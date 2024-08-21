from pip._vendor import requests

# 查询目标网址，基于开源项目：https://github.com/NateScarlet/holiday-cn
target_url = 'https://fastly.jsdelivr.net/gh/NateScarlet/holiday-cn@master/2024.json'

# 请求目标年份数据
response = requests.get(target_url.format(2024), timeout=10)
data = response.json()
print(data['days'])
