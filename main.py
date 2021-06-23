# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
from flask_restful import Api, Resource
from flask import request
from flask_sqlalchemy import SQLAlchemy
import LocateShareAPI
import UserManagerAPI
from config import db

app = Flask(__name__)


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
    return UserManagerAPI.login_api(username, password)

@app.route('/signUp', methods=['POST'])
def signUp():
    return


if __name__ == "__main__":
    app.run(debug=True)
