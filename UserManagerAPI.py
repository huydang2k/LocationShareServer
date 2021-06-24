from models import db, User

# Input: username, hashed_password
# Output: user hoặc none nếu username và password sai
def login_api(username, hashed_password):
    user = User.query.filter(User.username == username, User.password == hashed_password).first()
    if user is None:
        return None
    a = {"fullName":user.fullName, "avatarUrl":user.avatarUrl, "gender":user.gender, "age":user.age, "currntCity":user.currentCity}
    return a

def signup_api(username, password, fullName, avatarUrl, gender, age, currentCity):
    existing_user = User.query.filter(User.username == username).first()
    if existing_user is None:
        user = User(username, password, fullName, avatarUrl, gender, age, currentCity)
        db.session.add(user)
        db.session.commit()
        userReturn = User.query.filter(User.username == username).first()
        if userReturn is not None:
            a = {"fullName": userReturn.fullName, "avatarUrl": userReturn.avatarUrl, "gender": userReturn.gender, "age": userReturn.age,
                 "currntCity": userReturn.currentCity}
            return a
        else:
            return None
    else:
        return None