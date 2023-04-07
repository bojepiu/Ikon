import database._init_ as DB

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
        return result
    except Exception as e:
        print(str(e))
        return "ERROR"

def update_user(id,name,email,password='',role=2):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_user',(id,name,email,password,role,''))
        return output[5]
    except Exception as e:
        print(str(e))
        return "ERROR"

def insert_user(name,email,password,role):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_user',(name,email,password,role,''))
        return output[4]
    except Exception as e:
        print(str(e))
        return "ERROR"
    
def delete_user(id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_user',(id,''))
        print(output)
        return output[1]
    except Exception as e:
        print(str(e))
        return "ERROR"


# insert_user('name_1','email_1','pass_1',1)
#insert_user('name_2','email_2','pass_2',2)
# update_user(2,'name_11','email_11','',1)
# update_user(18,'name_22','email_22','2222',1)
# get_all_users()
# validate_user_pass('name_22','2222')
# delete_user('asd')
# CONNECTION.close()