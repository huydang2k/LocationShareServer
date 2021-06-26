from models import User, Key
from config import db


def search_api(userId, currentCity):
    update_locate_api(userId, currentCity)
    sql = "SELECT User.* FROM User JOIN Key as k1 on User.userId = k1.userId1" \
          " JOIN Key as k2 on User.userId = k2.userId2" \
          " WHERE k1.userId1 = %s or k2.userId2 = %s"
    params = (userId, userId)

    # users = db.engine.execute("SELECT User.* FROM User, Key WHERE User.userId = Key.userId1 or User.userId = Key.userId2")
    # for u in users:
    #     print(u["userId"])
    #
    # return {"userId": userid, "cityId": cityId}

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

