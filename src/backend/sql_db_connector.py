import pymysql


def connect_to_database(username, password):
    try:
        return pymysql.connect(host='localhost',
                               user=username,
                               password=password,
                               database='travel_itinerary',
                               charset='utf8mb4')
    except pymysql.Error as e:
        code, msg = e.args
        print("Cannot connect to the database", code, msg)
        return None
