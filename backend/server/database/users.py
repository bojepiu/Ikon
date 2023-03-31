import _init_ as DB

CONNECTION = DB.init_connection()

def validate_user_pass(user,pwd):
    try:
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
    
def get_all_users():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_users')
        x = cursor.stored_results()
        for i in x:
            result=i.fetchall()
        print(result)
        return "OK"
    except Exception as e:
        print(str(e))
        return "ERROR"

def update_user(id,name,email,password='',role=2):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_user',(id,name,email,password,role,''))
        print(output[5])
        return 'OK'
    except Exception as e:
        print(str(e))
        return "ERROR"

def insert_user(name,email,password,role):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_user',(name,email,password,role,''))
        print(output[4])
        return "OK"
    except Exception as e:
        print(str(e))
        return "ERROR"
    
def delete_user(id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_user',(id,''))
        return output[1]
    except Exception as e:
        return "ERROR"


#insert_user('name_1','email_1','pass_1',1)
#insert_user('name_2','email_2','pass_2',2)
#update_user(17,'name_11','email_11','mypass2',1)
# update_user(18,'name_22','email_22','2222',1)
# get_all_users()
# validate_user_pass('name_22','2222')
#delete_user(16)
# CONNECTION.close()