# import requests
# import time

# # data1 = {"username": "duongdt", "password": "123456"}
# # response1 = requests.post("http://127.0.0.1:5000/login", json=data1).json()
# # print(response1)

# # data2 = {"username": "maitruongson", "password": "123456", "birthYear": 1999, "avatarUrl": "",
# #          "currentCity": "Haiduong", "gender": 0, "fullName": "MTS"}
# #
# # response2 = requests.post("http://127.0.0.1:5000/signUp", json=data2).json()
# # print(response2)

# # data3 = {"userId": 1, "currentCity": "1000"}
# # response3 = requests.post("http://127.0.0.1:5000/update_locate", json=data3).json()
# # print(response3)

# data4 = {"userId": 1, "currentCity": "1000"}
# response4 = requests.get("http://127.0.0.1:5000/search", json=data4).json()
# print(response4)

# # from LocateShareAPI import search_api
# # res = search_api(1, "4431")
# # print(res)

# # from config import db
# # cursor = db.cursor()
# # sql = "SELECT u.*, k.commonKey FROM User u, CommonKey k " \
# #               "WHERE (u.userId = k.userId1 AND k.userId2 = %s) OR (u.userId = k.userId2 AND k.userId1 = %s) " \
# #               "ORDER BY u.userId ASC"
# # params = (1, 1)
# # cursor.execute(sql, params)
# # results = cursor.fetchall()
# # # print(len(results))
# # for x in results:
# #     print(x[0])

# # from KeyAPI import add_key
# # resp = add_key(1, 15)
# # print(resp)