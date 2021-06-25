# from config import db

# Models
class User:
    # id = db.Column('userId', db.Integer, primary_key=True, autoincrement=True)
    # username = db.Column(db.String(45))
    # password = db.Column(db.String(45))
    # fullName = db.Column(db.String(100))
    # avatarUrl = db.Column(db.String(100))
    # gender = db.Column(db.Integer)
    # birthYear = db.Column(db.Integer)
    # currentCity = db.Column(db.String(45))
    def __init__(self, username, password, fullName, avatarUrl, gender, birthYear, currentCity):
        self.username = username,
        self.password = password,
        self.fullName = fullName,
        self.avatarUrl = avatarUrl,
        self.gender = gender,
        self.birthYear = birthYear,
        self.currentCity = currentCity


class Key:
    # userId1 = db.Column(db.Integer, primary_key=True)
    # userId2 = db.Column(db.Integer, primary_key=True)
    # commonKey = db.Column(db.String(12), unique=True)

    def __init__(self, id1, id2, key):
        self.userId1 = id1,
        self.userId2 = id2,
        self.commonKey = key


# db.create_all