import database._init_ as DB

def get_all_sessions():
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_sessions')
        for i in cursor.stored_results():
            result=i.fetchall()
            return result
        return []
    except Exception as e:
        CONNECTION.close()
        return 'ERROR'
    finally:
        CONNECTION.close()
    
def insert_session(module_id,name):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_session',(module_id,name,''))
        print(output)
        return output[2]
    except Exception as e:
        if str(e).split(' ')[0]=='1452':
            return "ID_NOT_FOUND"
        return 'ERROR'
    finally:
        CONNECTION.close()

def update_session(id,module_id,name):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_session',(id,module_id,name,''))
        print(output)
        return output[3]
    except Exception as e:
        if e.args[0]== 1452:
            return "MODULE_NOT_FOUND"
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()
    
#Al eliminar session se eliminan las sentencias????
#O hacer la pregunta
def delete_session(session_id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_session',(session_id,''))
        print(output)
        return []
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()
    
def get_sessions_by_module(module_id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_sessions_by_module',(module_id,))
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'
    finally:
        CONNECTION.close()
