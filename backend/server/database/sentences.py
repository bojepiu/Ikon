import _init_ as DB

CONNECTION=DB.init_connection()

def insert_sentence(session_id,text,order,image,audio,video,aux):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_sentence',(session_id,text,order,image,audio,video,aux,''))
        print('-_-')
        print(output)
        return []
    except Exception as e:
        print(str(e))
        return 'ERROR'
    
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



insert_sentence(1,"t2 t1 t2","2,1,3","imgenu1","audenu1","videoenu1","auxedun1")
get_all_sentences()