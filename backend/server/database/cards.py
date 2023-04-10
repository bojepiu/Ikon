import database._init_ as DB

CONNECTION = DB.init_connection()

def get_all_cards():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_cards')
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'

def insert_card(topic_id,text,image,audio,video,aux):
    try:
        cursor = CONNECTION.cursor()
        output=cursor.callproc('insert_card',(topic_id,text,image,audio,video,aux,''))
        return output[6]
    except Exception as e:
        print(str(e))
        #ERROR 1452 topic not found
        if e.args[0]== 1452:
            return "TOPIC_NOT_FOUND"
        return 'ERROR'

def update_card(id,topic_id,text,image,audio,video,aux):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_card',(id,topic_id,text,image,audio,video,aux,''))
        return output[7]
    except Exception as e:
        print(str(e))
        return 'ERROR'

#PENDIENTE VALIDAR QUE NO SE PUEDA BORRAR SI ESTA SIENDO USADA
def delete_card(id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_card',(id,''))
        return output[1]
    except Exception as e:
        print(str(e))
        return 'ERROR'


##SECTION ASSOCIATION
def get_cards_by_topic(topic_id):
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_cards_by_topic',(topic_id,))
        x = cursor.stored_results()
        result=''
        for i in x:
            result=i.fetchall()
        print(result)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'

# t1='t1'
# img1='image/1.jpg'
# aud1='audio/1.mp3'
# vid1='video/1.mp4'
# aux1='aux/1.jpg'
# insert_card(1,t1,img1,aud1,vid1,aux1)
# t2='t2'
# img2='image/2.jpg'
# aud2='audio/2.mp3'
# vid2='video/2.mp4'
# aux2='aux/2.jpg'
# insert_card(2,t2,img2,aud2,vid2,aux2)
# t3='t2'
# img3='image/3.jpg'
# aud3='audio/3.mp3'
# vid3='video/3.mp4'
# aux3='aux/3.jpg'
# insert_card(3,t2,img3,aud3,vid3,aux3)

#insert_card(4,t,img,aud,vid,aux)
# update_card(20,3,t,img,aud,vid,aux)
# delete_card(7)
# print(delete_card(1))
#get_all_cards()
# get_cards_by_topic(2)