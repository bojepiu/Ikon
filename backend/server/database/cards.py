import database._init_ as DB

def get_all_cards():
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_cards')
        for i in cursor.stored_results():
            result=i.fetchall()
            return result
        return []
    except Exception as e:
        return 'ERROR'
    finally:
        CONNECTION.close()

def insert_card(topic_id,text,image,audio,video,aux):
    try:
        CONNECTION = DB.init_connection()
        cursor = CONNECTION.cursor()
        output=cursor.callproc('insert_card',(topic_id,text,image,audio,video,aux,''))
        return output[6]
    except Exception as e:
        print(str(e))
        #ERROR 1452 topic not found
        if e.args[0]== 1452:
            return "TOPIC_NOT_FOUND"
        return 'ERROR'
    finally:
        CONNECTION.close()

def update_card(id,topic_id,text,image,audio,video,aux):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_card',(id,topic_id,text,image,audio,video,aux,''))
        return output[7]
    except Exception as e:
        print(str(e))
        if str(e).split(' ')[0]=='1452':
            return "TOPIC_NOT_FOUND"
        return 'ERROR'
    finally:
        CONNECTION.close()

def delete_card(id):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_card',(id,''))
        return output[1]
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()

def get_cards_by_topic(topic_id):
    try:
        CONNECTION = DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_cards_by_topic',(topic_id,))
        x = cursor.stored_results()
        result=''
        for i in x:
            result=i.fetchall()
        print(result)
        return result
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()
