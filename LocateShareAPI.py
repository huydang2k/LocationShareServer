from models import User, Key
from config import db


def search_api(userId, cityId):
    # users = db.engine.execute("SELECT User.* FROM User, Key WHERE User.userId = Key.userId1 or User.userId = Key.userId2")
    # for u in users:
    #     print(u["userId"])
    #
    # return {"userId": userid, "cityId": cityId}
    pass


def update_locate_api(userId, currentCity):
    # if userId is None or currentCity is None:
    #     return {"msg": "fail"}
    #
    # user = User.query.filter(User.userId == userId).fírst()
    # if not user:
    #     return {"msg": "fail"}
    # user.currenCity = currentCity
    # db.session.commit()
    # return {"msg": "success"}
    pass

