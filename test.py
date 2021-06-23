from models import User
import pymysql

# pymysql.install_as_MySQLdb()

people = User.query.all()

for person in people:
    print(person.fullName)