import requests
import random

# 定义目标 URL
url = "http://yanwan.store/run4/mi20240807.php"

random_number = random.randint(10000, 20000)

# 定义要发送的参数
data = {
    "user": "2286550378@qq.com",
    "password": "sunsuo123@ql",
    "step": random_number,
    "ver": "cxydzsv3.2"
}

# 定义请求头，包括 User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# 发送 POST 请求
response = requests.post(url, data=data, headers=headers)

random_number = random.randint(10000, 20000)

# 定义要发送的参数
data = {
    "user": "19707733786@163.com",
    "password": "t19707733786",
    "step": random_number,
    "ver": "cxydzsv3.2"
}

response = requests.post(url, data=data, headers=headers)

# 输出响应内容
print("状态码:", response.status_code)
print("响应内容:", response.text)
