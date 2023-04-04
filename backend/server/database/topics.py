import _init_ as DB

CONNECTION=DB.init_connection()

def get_all_topics():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_topics')
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'

def insert_topic(name):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_topic',(name,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'

def update_topic(id,name):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_topic',(id,name,''))
        print(output)
        return 'OK'
    except Exception as e:
        return 'ERROR'

def delete_topic(id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_topic',(id,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'


# insert_topic('first_topic')
# insert_topic('second_topic')
# insert_topic('third_topic')
get_all_topics()
# update_topic(2,'second_topic')
# delete_topic(3)