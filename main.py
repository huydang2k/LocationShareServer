# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from flask_restful import Api,Resource
from flask import request
from LocateShareAPI import search_api
from LocateShareAPI import update_locate_api
from UserManagerAPI import login_api
from UserManagerAPI import signup_api
app = Flask(__name__)

# api = Api(app)
#
# #api end points

@app.route('/search/<userid>/<cityId>',methods=['GET'])
def search(userid,cityId):
    assert userid == request.view_args['userid']
    assert cityId == request.view_args['cityId']

    return search_api(userid,cityId)

@app.route('/update_locate/<userid>/<cityId>',methods=['POST'])
def update_locate(userid,cityId):
    assert userid == request.view_args['userid']
    assert cityId == request.view_args['cityId']

    return update_locate_api(userid,cityId)
@app.route('/login',methods=['POST'])
def login():
    return
@app.route('/signUp',methods=['POST'])
def signUp():
    return
if __name__ == "__main__":
    app.run(debug=True)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
