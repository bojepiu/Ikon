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
    


insert_session('session-1',1)
get_all_sessions()