from config import db
import KeyAPI
import random

cursor = db.cursor()


def search_api(userId, currentCity):
    update_locate_api(userId, currentCity)
    try:
        sql = "SELECT u.*, k.commonKey FROM User u, CommonKey k " \
              "WHERE (u.userId = k.userId1 AND k.userId2 = %s) OR (u.userId = k.userId2 AND k.userId1 = %s) " \
              "ORDER BY u.userId ASC"
        params = (userId, userId)
        cursor.execute(sql, params)
        results = cursor.fetchall()
        data = [{"msg": "success"}]
        for u in results:
            # Update counter
            counter = u[-2]
            counter = counter + 1
            update_counter_api(u[0], counter)

            # Generate session key
            common_key = u[-1]
            k_0, k_1 = KeyAPI.generate_session_key(counter, common_key)

            # Calculate x_b, x_a, x
            r = random.randint(10000, 4000000000)
            b_current_city = int(u[-3])
            x_b = r * (b_current_city + k_0) + k_1
            x_a = currentCity + k_0
            x = r * x_a - x_b

            # Get result list
            if x + k_1 == 0:
                today = date.today()
                yearNow = today.year
                data.append({
                    "fullName": u[3],
                    "age": yearNow - u[6],
                    "gender": u[5],
                    "avatarUrl": u[4]
                })
        return data
    except:
        return {"msg": "fail"}


def update_locate_api(userId, currentCity):
    sql = "UPDATE User SET currentCity = %s WHERE userId = %s"
    params = (currentCity, userId)
    try:
        cursor.execute(sql, params)
        db.commit()
        return {"msg": "success"}
    except:
        return {"msg": "fail"}


def update_counter_api(userId, counter):
    sql = "UPDATE User SET counter = %s WHERE userId = %s"
    params = (counter, userId)
    try:
        cursor.execute(sql, params)
        db.commit()
        return {"msg": "success",
                "userId": userId,
                "counter": counter}
    except:
        return {"msg": "fail"}