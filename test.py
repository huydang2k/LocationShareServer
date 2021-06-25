# import requests
import mysql.connector
from models import User
# data1 = {'username': "duongdt", 'password': "123456"}
# response1 = requests.post('http://127.0.0.1:5000/login', json=data1).json()
# print(response1)
# data2 = {'username': None, 'password': '123456', 'birthYear': 1999, 'avatarUrl': None, 'currentCity': 'Haiduong', 'gender': '1', 'fullName': None}
# response2 = requests.post('http://127.0.0.1:5000/signUp', json=data2).json()
# print(response2)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="db_share_location"
)

cursor = db.cursor()

sql = "INSERT INTO User(username, password, fullName, avatarUrl, gender, birthYear, currentCity) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s)"
username = "son"
password = "123456"
fullName = "maitruongson"
avatarUrl = None
gender = 0
birthYear = 2000
currentCity = "Haiphong"
params = (username, password, fullName, None, gender, birthYear, currentCity)
try:
    cursor.execute(sql, params)
    db.commit()
    print(cursor.getlastrowid())
except:
    print("fail")


