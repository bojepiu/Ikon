import database._init_ as DB

def validate_user_pass(user,pwd):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('validate_user',(user,pwd))
        x=cursor.stored_results()
        for i in x:
            result=i.fetchall()
        if len(result):
            return result[0]
        else: return "BAD_CREDENTIALS"
    except Exception as e:
        print(str(e))
        return 'DATABASE_ERROR'
    finally:
        CONNECTION.close()
    
def get_all_users():
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_users')
        x = cursor.stored_results()
        for i in x:
            result=i.fetchall()
        return result
    except Exception as e:
        print(str(e))
        return "ERROR"
    finally:
        CONNECTION.close()

def update_user(id,name,email,password='',role=2):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_user',(id,name,email,password,role,''))
        return output[5]
    except Exception as e:
        print(str(e))
        return "ERROR"
    finally:
        CONNECTION.close()

def insert_user(name,email,password,role):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_user',(name,email,password,role,''))
        return output[4]
    except Exception as e:
        print(str(e))
        return "ERROR"
    finally:
        CONNECTION.close()
    
def delete_user(id):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_user',(id,''))
        print(output)
        return output[1]
    except Exception as e:
        print(str(e))
        return "ERROR"
    finally:
        CONNECTION.close()
