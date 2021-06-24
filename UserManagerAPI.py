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
         "age": yearNow - user.birthYear, "currentCity": user.currentCity}
    return a


def signup_api(username, password, fullName, avatarUrl, gender, birthYear, currentCity):
    existing_user = User.query.filter(User.username == username).first()
    if existing_user is None:
        user = User(username, password, fullName, avatarUrl, gender, birthYear, currentCity)
        db.session.add(user)
        db.session.commit()
        userReturn = User.query.filter(User.username == username).first()
        if userReturn is not None:
            a = {"msg": "true", "fullName": userReturn.fullName, "avatarUrl": userReturn.avatarUrl,
                 "gender": userReturn.gender, "age": yearNow - userReturn.age, "currentCity": userReturn.currentCity}
            return a
        else:
            return {"msg": "fail"}
    else:
        return {"msg": "fail"}
