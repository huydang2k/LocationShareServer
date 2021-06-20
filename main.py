# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

#api
class Hello(Resource):
    def get(self):
        return {"data":"hello"}
api.add_resource(Hello,"/h")
if __name__ == "__main__":
    #app.run(debug=True)

    print(loc)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
