import _init_ as DB

CONNECTION=DB.init_connection()

def get_all_sessions():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_sessions')
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'
    
def insert_session(name,module_id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_session',(name,module_id,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'

def update_session(session_id,module_id,name):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_session',(session_id,module_id,name,''))
        print(output)
        return 'OK'
    except Exception as e:
        #1452 module not found
        print(str(e))
        return 'ERROR'
    
#Al eliminar session se eliminan las sentencias????
#O hacer la pregunta
def delete_session(session_id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_session',(session_id,''))
        print(output)
        return []
    except Exception as e:
        print(str(e))
        return 'ERROR'
    
def get_sessions_by_module(module_id):
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_sessions_by_module',(module_id,))
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'


# insert_session('session-1',4)
# update_session(1,2,'other_name')
# delete_session(2)
# get_sessions_by_module(1)
get_all_sessions()