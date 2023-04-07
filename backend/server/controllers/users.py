import re
import database.users as db


email_pattern=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def validate_user(username,password):
    if len(password) < 8:
        return {"error":"password_length"}
    result=db.validate_user_pass(username,password)
    if result == "BAD_CREDENTIALS":
        return {"error":"user/pass failed"}
    if result == "ERROR":
        return {"error":"database_error"}
    return {"username":result[0],"email":result[1],"role":result[2]}

def create_user(username,email,password,role):
    if len(password) < 8:
        return {"error":"password_length"}
    if role != 1 and role != 2:
        return {"error":"role_failed"}
    if not  re.fullmatch(email_pattern, email):
        return {"error":"bad_email"}
    new_user=db.insert_user(username,email,password,role)
    if new_user == 'ALREADY_EXISTS':
        return {"error":"user_duplicated"}
    if new_user == 'ERROR':
        return {"error":"error_database"}
    return {"message":"user_created"}
    
def  update_user(userid,username,email,password='',role=2):
    if not isinstance(userid,int):
        return {"error":"bad_userid"}
    if len(password) < 8 and password != '':
        return {"error":"password_length"}
    if role != 1 and role != 2:
        return {"error":"role_failed"}
    if not  re.fullmatch(email_pattern, email):
        return {"error":"bad_email"}
    up_user=db.update_user(userid,username,email,password,role)
    if up_user == 'ALREADY_EXISTS':
        return {"error":"user_duplicated"}
    if up_user != "SUCCESS":
        return {"error":"update_failed"}
    return {"message":"user_updated"}

def delete_user(userid):
    if not isinstance(userid,int):
        return {"error":"bad_userid"}
    if db.delete_user(userid) != 'SUCCESS':
        return {"error":"database_error"}
    return {"message":"user_deleted"}

def get_all_users():
    result=db.get_all_users()
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"users":[],"total":len(result)}
        for user in result:
            data["users"].append({"userid":user[0],"username":user[1],"email":user[2],"role":user[3]})
        return data
 
# print(create_user('asdasd','emaislm@asdal.co','paasdssmal',1))
# z=get_all_users()
# print(z)
# print(delete_user(4))
# print(validate_user('asdasd','paasdssmal'))
# print(update_user(3,'admin','emaislm@asdal.co','',2))

