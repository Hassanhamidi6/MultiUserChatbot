import sqlite3 
from datetime import datetime

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

def is_user_exists(user_id) ->bool:
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    query  = f"SELECT * FROM USERS WHERE user_id ={user_id}"
    cursor.execute(query)
    data = cursor.fetchone()
    if len(data) > 0:
        return True
    else:
        return False

def is_email_exists(email) ->bool:
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    query  = f"SELECT * FROM USERS WHERE email ={email}"
    cursor.execute(query)
    data = cursor.fetchone()
    if len(data) > 0:
        return True
    else:
        return False




def create_user(user_id):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()
    
    user = f"user_{user_id}"
    query = f"CREATE TABLE IF NOT EXISTS {user}(session_id Integer Primary key,session_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"

    cursor.execute(query)
    connection.commit()
    connection.close()

def is_session_exists(user_id,session_id):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()
    
    table_name =f"user_{user_id}"
    query  = f"SELECT * FROM {table_name} WHERE session_id ={session_id}"
    cursor.execute(query)
    data = cursor.fetchone()
    if len(data) > 0:
        return True
    else:
        return False
    
def insert_session_info(session_id,user_id):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    table_name = f"user_{user_id}"
    query = f"INSERT INTO {table_name}(session_id) VALUES (?)"
    cursor.execute(query,(session_id))
    connection.commit()
    connection.close()


def create_session(session_id):
    table_name = f"session_{session_id}"
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    query = f"CREATE TABLE IF NOT EXISTS {table_name}(query varchar(5000),response varchar(5000),time TIMESTAMP DEAFULT CURRENT_TIMESTAMP)"
    cursor.execute(query)
    connection.commit()
    connection.close()

def insert_chat(session_id,user_query,response):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()
    
    table_name =f"session_{session_id}"
    query = f"INSERT INTO {table_name}(query,response) VALUES(?,?)"
    cursor.execute(query,(user_query,response))
    connection.commit()
    connection.close()

def get_chat_history(session_id):
    connection = sqlite3.connect("Maindb.db")
    cursor = connection.cursor()
    table_name = f"session_{session_id}"
    query =f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data


def resend_otp(user_id, new_otp):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    current_time = datetime.now()

    query = """
    UPDATE USERS
    SET OTP = ?, OtpTime = ?
    WHERE user_id = ?
    """

    cursor.execute(query, (new_otp, current_time, user_id))
    connection.commit()
    connection.close()

def verify_otp(user_id,otp):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()
    
    #IsOtpExists

    #ISOtpExpired

    #IsOtpMatched

def IsOtpExpired(user_id):
    connection = sqlite3.connect("MainDb.db")
    cursor = connection.cursor()

    query =f"SELECT OtpTime from USERS WHERE user_id ={user_id}"
    cursor.execute(query)
    data = cursor.fetchone()  
    generated_time = data[0]
    current_time = datetime.now()

    expiration_limit = 60

    if((current_time-generated_time>expiration_limit)):
        return True 
    else:
        return False

def IsOtpMatched():
    pass