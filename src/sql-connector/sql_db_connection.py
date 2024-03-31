import pymysql


def make_db_connection(uname, pswrd, db_name):
    try:
        return pymysql.connect(host='localhost',
                               user=uname,
                               password=pswrd,
                               database=db_name,
                               charset='utf8mb4')

    except pymysql.Error as e:
        code, msg = e.args
        print("Cannot connect to the database", code, msg)
