# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
from flask_restful import Api, Resource
from flask import request
from flask_sqlalchemy import SQLAlchemy
import LocateShareAPI
import UserManagerAPI

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/db_share_location'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column('userId', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    fullName = db.Column(db.String(100))
    avatarUrl = db.Column(db.String(100))
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    currentCity = db.Column(db.String(45))

    def __init__(self, username, password, fullName, avatarUrl, gender, age, currentCity):
        self.username = username,
        self.password = password,
        self.fullName = fullName,
        self.avatarUrl = avatarUrl,
        self.gender = gender,
        self.age = age,
        self.currentCity = currentCity

# class Key(db.Model):
#     userId1 = db.Column(db.Integer)
#     userId2 = db.Column(db.Integer)
#     commonKey = db.Column(db.String(12), unique=True)
#
#     def __init__(self, id1, id2, key):
#         self.userId1 = id1,
#         self.userId2 = id2,
#         self.commonKey = key

db.create_all()
def login_api(username, hashed_password):
    user = User.query.filter(User.username == username, User.password == hashed_password).first()
    a = {"fullName":user.fullName}
    return a
@app.route('/search/<userid>/<cityId>', methods=['GET'])
def search(userid, cityId):
    assert userid == request.view_args['userid']
    assert cityId == request.view_args['cityId']
    return LocateShareAPI.search_api(userid, cityId)


@app.route('/update_locate/<userid>/<cityId>', methods=['POST'])
def update_locate(userid, cityId):
    assert userid == request.view_args['userid']
    assert cityId == request.view_args['cityId']
    return LocateShareAPI.update_locate_api(userid, cityId)

@app.route('/login/<username>/<password>', methods=['GET'])
def login(username, password):
    assert username == request.view_args['username']
    assert password == request.view_args['password']
    return login_api(username, password)

@app.route('/signUp', methods=['POST'])
def signUp():
    return

if __name__ == "__main__":
    app.run(debug=True)
