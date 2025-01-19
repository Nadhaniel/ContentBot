import MySQLdb as sql
import sshtunnel as ssh
import os

ssh.SSH_TIMEOUT = 10.0
ssh.TUNNEL_TIMEOUT = 10.0

#Database connection management functions

def connect_run_func(func, *args):
    try:
        connection = sql.connect(
            host=os.getenv("SQL_HOST"),
            user=os.getenv("SQL_USER"),
            password=os.getenv("SQL_PASSWORD"),
            db=os.getenv("SQL_DATABASE_REDDITMAG")
        )
        print("Connection successful!")
        func(*args, connection=connection)
    except sql.Error as e:
        print("Error connecting to MySQL", e)
        connection.close()
    return connection

def ssh_connect_run_func(func, *args):
    with ssh.SSHTunnelForwarder(
            ('ssh.pythonanywhere.com'),
            ssh_username=os.getenv("SQL_USER"), ssh_password=os.getenv("PYTHON_ANYWHERE_PASS"),
            remote_bind_address=(os.getenv("SQL_HOST"), 3306)
    ) as tunnel:
        ssh_connection = sql.connect(
            user=os.getenv("SQL_USER"),
            passwd=os.getenv("SQL_PASSWORD"),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv("SQL_DATABASE_REDDITMAG"),
        )
        func(*args, connection=ssh_connection)
        ssh_connection.close()

def close_db(connection):
    try:
        connection.close()
        print("Connection closed!")
    except sql.Error as e:
        print("Error closing connection", e)

# Database manipulation functions

def insert_rows(row_data, connection=None):
    if connection is None:
        raise ValueError("SSH client is required for this operation.")
    else:
        cursor = connection.cursor()
        insert_query = "INSERT INTO relationship_advice (Title, SelfText, Score, URL) VALUES (%s, %s, %s, %s)"

        for dict in row_data:
            values = (dict.get("Title"), dict.get("Body"), dict.get("Score"), dict.get("URL"))
            try:
                cursor.execute(insert_query, values)
                connection.commit()
                print("Row inserted successfully!")
            except sql.Error as e:
                print("Error inserting row:", e)
                if connection:
                    connection.rollback()  # Rollback in case of error

        cursor.close()