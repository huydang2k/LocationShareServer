from Crypto.Cipher import AES
import random


def generate_common_key():
    i = 1
    common_key = ""
    while i <= 10:
        common_key = common_key + str(random.randint(0, 9))
        i = i+1
    return common_key


def add_key(userId1, userId2):
    existing_key = Key.query.filter(Key.userId1 == userId1, Key.userId2 == userId2).first()
    if existing_key is None:
        return {"msg": "failed"}
    else:
        common_key = generate_common_key()
        new_key = Key(userId1, userId2, common_key)
        db.session.add(new_key)
        db.session.commit()
        added_key = Key.query.filter(Key.userId1 == userId1, Key.userId2 == userId2)
        return {"msg": "success", "userId1": added_key.userId1, "userId2": added_key.userId2}


def generate_session_key(counter, common_key):
    common_key = int(common_key)
    # cipher = AES(counter, common_key)
    return k_0, k_1
