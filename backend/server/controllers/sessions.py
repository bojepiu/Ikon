import database.sessions as db


def create_session(name,module_id):
    if not isinstance(module_id,int):
        return {"error":"bad_module_id"}
    new_session=db.insert_session(name,module_id)
    if new_session == 'DUPLICATED':
        return {"error":"session_duplicated"}
    if new_session == 'ID_NOT_FOUND':
        return {"error":"module_id_not_found"}
    if new_session == 'ERROR':
        return {"error":"error_database"}
    return {"message":"session_created"}
    
def  update_session(id,module_id,name):
    if not isinstance(id,int):
        return {"error":"bad_id"}
    if not isinstance(module_id,int):
        return {"error":"bad_module_id"}
    up_session=db.update_session(id,module_id,name)
    print(up_session)
    if up_session == 'DUPLICATED':
        return {"error":"session_duplicated"}
    if up_session == 'ID_NOT_FOUND' or up_session == 'MODULE_ID_NOT_FOUND':
        return {"error":up_session.lower()}
    if up_session != "SUCCESS":
        return {"error":"update_failed"}
    return {"message":"session_updated"}

def delete_session(id):
    if not isinstance(id,int):
        return {"error":"bad_session_id"}
    result = db.delete_session(id)
    if  result == 'ERROR':
        return {"error":"database_error"}
    if result == "USED_TOPIC":
        return {"error":"used_session"}
    return {"message":"session_deleted"}

def get_all_sessions():
    result=db.get_all_sessions()
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"sessions":[],"total":len(result)}
        for session in result:
            data["sessions"].append({"id":session[0],"module_id":session[1],"name":session[2]})
        return data

def get_sessions_by_module(module_id):
    if not isinstance(module_id,int):
        return {"error":"bad_module_id"}
    result=db.get_sessions_by_module(module_id)
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"sessions":[],"total":len(result)}
        for session in result:
            data["sessions"].append({"id":session[0],"module_id":session[1],"name":session[2]})
        return data