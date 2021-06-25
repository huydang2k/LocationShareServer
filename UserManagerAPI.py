from models import db, User
import responses
from datetime import date

today = date.today()
yearNow = today.year


def login_api(username, hashed_password):
    user = User.query.filter(User.username == username, User.password == hashed_password).first()
    if user is None:
        return {"msg": "fail"}
    a = {"msg": "true", "fullName": user.fullName, "avatarUrl": user.avatarUrl, "gender": user.gender,
         "age": yearNow - user.birthYear, "currentCity": user.currentCity, 'userID': user.id}
    return a


def signup_api(username, password, fullName, avatarUrl, gender, birthYear, currentCity):
    if username is None:
        return {"msg": "fail"}
    if password is None:
        return {"msg": "fail"}
    if fullName is None:
        return {"msg": "fail"}
    if gender is None:
        return {"msg": "fail"}
    if currentCity is None:
        return {"msg": "fail"}
    existing_user = User.query.filter(User.username == username).first()
    if existing_user is None:
        user = User(username, password, fullName, avatarUrl, gender, birthYear, currentCity)
        db.session.add(user)
        db.session.commit()
        userReturn = User.query.filter(User.username == username).first()
        if userReturn is not None:
            a = {"msg": "true", "fullName": userReturn.fullName, "avatarUrl": userReturn.avatarUrl,
                 "gender": userReturn.gender, "age": yearNow - userReturn.birthYear,
                 "currentCity": userReturn.currentCity, "userID": userReturn.id}
            return a
        else:
            return {"msg": "fail"}
    else:
        return {"msg": "fail"}
