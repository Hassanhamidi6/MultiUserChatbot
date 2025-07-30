import sqlite3 

import sqlite3

def create_tables():
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS USERS (
        user_id INTEGER PRIMARY KEY,
        user_name VARCHAR(20),
        email VARCHAR(40),
        OTP INTEGER,
        OtpTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Isverified INTEGER DEFAULT 0
    )
    """

    cursor.execute(query)
    connection.commit()
    connection.close()


def insert_user(user_id,email,name,otp):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()
    query = """
    INSERT INTO USER(user_id,user_name,email,OTP) VALUES
    (?,?,?,?)
    """
    cursor.execute(query,(user_id,email,name,otp))
    connection.commit()
    connection.close()


def create_user(user_id):
    pass


