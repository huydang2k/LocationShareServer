# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
from flask_restful import Api, Resource
from flask import request
from flask_sqlalchemy import SQLAlchemy
from config import app, db
import LocateShareAPI
import UserManagerAPI

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

@app.route('/login', methods=['POST'])
def login():
    j = request.get_json(force=True)
    return UserManagerAPI.login_api(j['username'], j['password'])

@app.route('/signUp', methods=['POST'])
def signUp():
    j = request.get_json(force=True)
    username = j['username']
    password = j['password']
    fullName = j['fullName']
    avatarUrl = j['avatarUrl']
    gender = j['gender']
    birthYear = j['birthYear']
    currentCity = j['currentCity']
    return UserManagerAPI.signup_api(username, password, fullName, avatarUrl, gender, birthYear, currentCity)

if __name__ == "__main__":
    app.run(debug=True)
