import database._init_ as DB

def get_all_modules():
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_modules')
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'
    finally:
        CONNECTION.close()
    
def insert_module(name,description):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_module',(name,description,''))
        print(output)
        return output[2]
    except Exception as e:
        if str(e).split(' ')[0]=='1452':
            return "ID_NOT_FOUND"
        return 'ERROR'
    finally:
        CONNECTION.close()

def update_module(module_id,name,description):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_module',(module_id,name,description,''))
        print(output)
        return output[3]
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()

def delete_module(module_id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_module',(module_id,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()
    