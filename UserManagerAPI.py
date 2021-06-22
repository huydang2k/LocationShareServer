from models import User
from config import db

#Input: username, hashed_password
#Output: user hoặc none nếu username và password sai
def login_api(username, hashed_password):
    user = User.query.filter(User.username == username, User.password == hashed_password).first()
    return user

def signup_api(username, password, fullName, avatarUrl, gender, age, currentCity):
    existing_user = User.query.filter(User.username == username).first()
    if existing_user is None:
        user = User(username, password, fullName, avatarUrl, gender, age, currentCity)
        db.session.add(user)
        db.session.commit()
        userReturn = User.query.filter(User.username == username).first()
        return userReturn
    else:
        return None