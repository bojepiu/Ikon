import database._init_ as DB

def insert_sentence(session_id,text,order,image,audio,video,aux):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_sentence',(session_id,text,order,image,audio,video,aux,''))
        CONNECTION.close()
        print(output)
        if str(output[7]) == "DUPLICATED" or output[7]=="CARD_NOT_FOUND" or output[7]=="SESSION_NOT_FOUND":
            return output[7]
        sentence_id=int(output[7])
        for card_id in order.split(','):
            result=insert_cards_sentences(card_id, sentence_id)
            print(result)
            if result !="SUCCESS":
                return result
        return "SUCCESS"
    except Exception as e:
        if str(e).split(' ')[0]=='1452':
            return "SESSION_NOT_FOUND"
        print(str(e))
        return 'ERROR'
    finally:
        if(CONNECTION.is_connected()):
            CONNECTION.close()

def insert_cards_sentences(card_id,sentence_id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        print(int(card_id),int(sentence_id))
        output=cursor.callproc('insert_cards_sentences',(int(card_id),int(sentence_id),''))
        if output[2] == "CARD_NOT_FOUND" or output[2] == "SENTENCE_NOT_FOUND":
            delete_sentence(sentence_id) 
            return output[2]
        return "SUCCESS"
    except Exception as e:
        print(str(e))
        r=delete_sentence(sentence_id)
        print(r)
        if str(e).split(' ')[0]=='1452':
            return "CARD_NOT_FOUND"
    finally:
        CONNECTION.close()

#Al actualizar la sentencia se elimina de la tabla relacion? o solo se actualiza?
def update_sentence(sentence_id,session_id,text,order,image,audio,video,aux):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_sentence',(sentence_id,session_id,text,order,image,audio,video,aux,''))
        print(output[8])
        return output[8]
    except Exception as e:
        print(e)
        return 'ERROR'
    finally:
        CONNECTION.close()
    
def delete_sentence(sentence_id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_sentence',(sentence_id,''))
        print(output)
        return output[1]
    except Exception as e:
        print(str(e))
        return 'ERROR'
    finally:
        CONNECTION.close()

def get_sentences_by_session(session_id):
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_sentences_by_session',(session_id,))
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
        return result
    except Exception as e:
        print(str(e))
        return "ERROR"
    finally:
        CONNECTION.close()
    
def get_all_sentences():
    try:
        CONNECTION=DB.init_connection()
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_sentences')
        for i in cursor.stored_results():
            result=i.fetchall()
            return result
    except Exception as e:
        return 'ERROR'
    finally:
        CONNECTION.close()
