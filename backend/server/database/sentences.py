import _init_ as DB

CONNECTION=DB.init_connection()

def insert_sentence(session_id,text,order,image,audio,video,aux):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_sentence',(session_id,text,order,image,audio,video,aux,''))
        print(output)
        return []
    except Exception as e:
        #1452 session doesn't exist
        print(str(e))
        return 'ERROR'

#Al actualizar la sentencia se elimina de la tabla relacion? o solo se actualiza?
def update_sentence(sentence_id,session_id,text,order,image,audio,video,aux):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_sentence',(sentence_id,session_id,text,order,image,audio,video,aux,''))
        print(output)
        return 'ok'
    except Exception as e:
        return 'fail'
    
def delete_sentence(sentence_id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_sentence',(sentence_id,''))
        print(output)
        return 'ok'
    except Exception as e:
        return 'fail' 

def get_sentences_by_session(session_id):
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_sentences_by_session',(session_id,))
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return 'ok'
    except Exception as e:
        print(str(e))
        return 'fail'
    
def get_all_sentences():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_sentences')
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'



insert_sentence(4,"t2 t2 text1","2,3,4","imgenu2","audenu2","videoenu2","")
# update_sentence(1,1,"t1 t1 t2 t1","1,1,3,2","imgenu2","audenu2","videoenu2","xd2")
# delete_sentence(1)
get_sentences_by_session(1)
get_all_sentences()