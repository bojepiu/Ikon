import database._init_ as DB

CONNECTION=DB.init_connection()

def insert_sentence(session_id,text,order,image,audio,video,aux):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_sentence',(session_id,text,order,image,audio,video,aux,''))
        print(output)
        return output[7]
    except Exception as e:
        #1452 session doesn't exist
        print(str(e))
        return 'ERROR'

#Al actualizar la sentencia se elimina de la tabla relacion? o solo se actualiza?
def update_sentence(sentence_id,session_id,text,order,image,audio,video,aux):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_sentence',(sentence_id,session_id,text,order,image,audio,video,aux,''))
        return output[8]
    except Exception as e:
        return 'ERROR'
    
def delete_sentence(sentence_id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_sentence',(sentence_id,''))
        return output[1]
    except Exception as e:
        print(str(e))
        return 'ERROR' 

def get_sentences_by_session(session_id):
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_sentences_by_session',(session_id,))
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
        return result
    except Exception as e:
        print(str(e))
        return "ERROR"
    
def get_all_sentences():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_sentences')
        for i in cursor.stored_results():
            result=i.fetchall()
            return result
    except Exception as e:
        return 'ERROR'



#insert_sentence(4,"t1 text1 text1","2,4,4","imgenu2","audenu2","videoenu2","")
update_sentence(7,4,"t1 text1 text1","2,4,4","imgenu2","audenu2","videoenu2","xd")
# delete_sentence(1)
# get_sentences_by_session(1)
get_all_sentences()