from models import User
import UserManagerAPI

people = User.query.all()

for person in people:
    print(person.fullName)

a = UserManagerAPI
print(a.login_api("sonmt", "123456"))
print(a.signup_api("bot7", "123456", "Bot 7", None, 1, 22, "Hanoi"))


