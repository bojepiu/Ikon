import mysql.connector
from dotenv import load_dotenv
import os

#Initialized env vars
load_dotenv()
HOST=os.getenv('DB_HOST')
PORT=int(os.getenv('DB_PORT'))
DATABASE=os.getenv('DB_NAME')
USER=os.getenv('DB_USER')
PASS=os.getenv('DB_PASS')


def init_connection():
    try:    
        connection = mysql.connector.connect(
        host =HOST,
        user =USER,
        passwd =PASS,
        database=DATABASE,
        port=PORT)
        return connection
    except Exception as e:
        print(str(e))
        return 'ERROR'

def close_connection(connection):
    try:
        connection.close()
        return "CLOSED"
    except Exception as e:
        print(str(e))
        return "ERROR"