import database._init_ as DB

def get_all_topics():
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_topics')
        for i in cursor.stored_results():
            result=i.fetchall()
            return result
        return []
    except Exception as e:
        return 'ERROR'
    finally:
        CONNECTION.close()

def insert_topic(name):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_topic',(name,''))
        return output[1]
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()

def update_topic(id,name):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_topic',(id,name,''))
        return output[2]
    except Exception as e:
        return 'ERROR'
    finally:
        CONNECTION.close()

def delete_topic(id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_topic',(id,''))
        return output[1]
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()
        