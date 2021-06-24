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
    assert username == request.json['username']
    print(username)
    assert password == request.json['password']
    return UserManagerAPI.login_api(username, password)

@app.route('/signUp/<username>/<password>/<fullName>/<avatarUrl>/<gender>/<age>/<currentCity>', methods=['GET'])
def signUp(username, password, fullName, avatarUrl, gender, age, currentCity):
    assert username == request.view_args['username']
    assert password == request.view_args['password']
    assert fullName == request.view_args['fullName']
    assert avatarUrl == request.view_args['avatarUrl']
    assert gender == request.view_args['gender']
    assert age == request.view_args['age']
    assert currentCity == request.view_args['currentCity']
    return UserManagerAPI.signup_api(username, password, fullName, avatarUrl, gender, age, currentCity)

if __name__ == "__main__":
    app.run(debug=True)
