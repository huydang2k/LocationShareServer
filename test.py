import requests

data = {'username': "duongdt", 'password': "123456"}
response = (requests.post('http://127.0.0.1:5000/login', json=data)).json()
print(response)
