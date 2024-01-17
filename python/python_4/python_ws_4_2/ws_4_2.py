import requests
from pprint import pprint as print


# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()
dummy_data =[]
for i in range(10):
    dummy_data.append(parsed_data[i]['name'])
print(dummy_data)
