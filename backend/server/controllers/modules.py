import database.modules as db


def create_module(name,description):
    new_module=db.insert_module(name,description)
    if new_module == 'DUPLICATED':
        return {"error":"module_duplicated"}
    if new_module == 'ERROR':
        return {"error":"error_database"}
    return {"message":"module_created"}
    
def  update_module(id,name,description):
    if not isinstance(id,int):
        return {"error":"bad_id"}
    up_module=db.update_module(id,name,description)
    print(up_module)
    if up_module == 'DUPLICATED':
        return {"error":"module_duplicated"}
    if up_module != "SUCCESS":
        return {"error":"update_failed"}
    return {"message":"module_updated"}

def delete_module(id):
    if not isinstance(id,int):
        return {"error":"bad_module_id"}
    result = db.delete_module(id)
    if  result == 'ERROR':
        return {"error":"database_error"}
    if result == "USED_TOPIC":
        return {"error":"used_module"}
    return {"message":"module_deleted"}

def get_all_modules():
    result=db.get_all_modules()
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"modules":[],"total":len(result)}
        for module in result:
            data["modules"].append({"id":module[0],"name":module[1],"description":module[2]})
        return data
