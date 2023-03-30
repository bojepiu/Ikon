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

CONNECTION=init_connection()

def validate_user_pass(user,pwd):
    try:
        if(CONNECTION == 'ERROR'):
            return 'DATABASE_ERROR'
        cursor=CONNECTION.cursor()
        cursor.callproc('validate_user',('admin','admin'))
        x=cursor.stored_results()
        for i in x:
            result=i.fetchall()
        print(result)
       
    except Exception as e:
        print(str(e))
        return 'DATABASE_ERROR'

validate_user_pass('admin','admin')
CONNECTION.close()