from models import User
import pymysql

# pymysql.install_as_MySQLdb()

import UserManagerAPI


people = User.query.all()

for person in people:
    print(person.fullName)

a = UserManagerAPI
print(a.login_api("duongdt", "123456"))
print(a.signup_api("bot7", "123456", "Bot 7", None, 1, 22, "Hanoi"))


