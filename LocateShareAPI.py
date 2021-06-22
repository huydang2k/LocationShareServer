from models import User
from models import Key
from config import db


def search_api(userid, cityId):
    user = User.query.filter()
    return {"userId": userid, "cityId": cityId}


def update_locate_api(userid, cityId):
    return {"update": "updated"}
