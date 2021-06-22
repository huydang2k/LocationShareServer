from models import User
from config import db


def login_api(username, hashed_password):
    user = User.query.filter_by(User.username == username, User.password == hashed_password) \
                .one_or_none()
    return user is not True


def signup_api(data):
    return