from models import User

people = User.query.all()

for person in people:
    print(person.fullName)