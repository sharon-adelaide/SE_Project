import mysql.connector as MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           password = "",
                           database = "ASHCROWDCOUNT")
    c = conn.cursor()

        

    return c, conn
		