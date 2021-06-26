from config import db
from datetime import date

cursor = db.cursor()


def login_api(username, hashed_password):
    sql = "SELECT * FROM User WHERE username = %s AND password = %s"
    params = (username, hashed_password)
    cursor.execute(sql, params)
    user = cursor.fetchone()
    today = date.today()
    yearNow = today.year
    if user is None:
        return {"msg": "fail"}
    return {
            "msg": "true",
            "data": {
                "userId": user[0],
                "username": user[1],
                "password": user[2],
                "fullName": user[3],
                "avatarUrl": user[4],
                "gender": user[5],
                "age": yearNow - user[6],
                "currentCity": user[7]
                }
            }


def signup_api(username, password, fullName, avatarUrl, gender, birthYear, currentCity):
    if username is None or password is None or \
            fullName is None or gender is None or \
            currentCity is None:
        return {"msg": "fail"}
    sql = "SELECT * FROM User WHERE username = %s"
    params = (username,)
    cursor.execute(sql, params)
    existing_user = cursor.fetchone()
    if existing_user is None:
        sql = "INSERT INTO User(username, password, fullName, avatarUrl, gender, birthYear, currentCity, counter) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 0)"
        params = (username, password, fullName, avatarUrl, gender, birthYear, currentCity)
        try:
            cursor.execute(sql, params)
            db.commit()
            userId = cursor.getlastrowid()
            today = date.today()
            yearNow = today.year
            return {
                    "msg": "success",
                    "data": {
                        "userId": userId,
                        "username": username,
                        "password": password,
                        "fullName": fullName,
                        "avatarUrl": avatarUrl,
                        "gender": gender,
                        "age": yearNow - birthYear,
                        "currentCity": currentCity
                        }
                    }
        except:
            return {"msg": "fail"}
    else:
        return {"msg": "fail"}
