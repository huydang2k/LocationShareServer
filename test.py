import requests

data1 = {"username": "duongdt", "password": "123456"}
response1 = requests.post("http://127.0.0.1:5000/login", json=data1).json()
print(response1)
data2 = {"username": "son4", "password": "123456", "birthYear": 1999, "avatarUrl": "",
         "currentCity": "Haiduong", "gender": 0, "fullName": "MTS"}
response2 = requests.post("http://127.0.0.1:5000/signUp", json=data2).json()
print(response2)