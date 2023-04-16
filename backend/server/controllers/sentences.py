import database.sentences as db
HTTP='http'

#Validar que contengan o vacio o http o https
def create_sentence(session_id,text,order,image,audio,video,aux):
    if not isinstance(session_id,int):
        return {"error":"bad_session_id"}
    print(len(text))
    if len(text) < 1:
        return {"error":"bad_text"}
    if len(image) < 1:
        return {"error":"bad_image"}
    # if not image.__contains__('http'):
    #     return {"error":"bad_image"}
    new_sentence=db.insert_sentence(session_id,text,order,image,audio,video,aux)
    print(new_sentence)
    if new_sentence == 'DUPLICATED':
        return {"error":"sentence_duplicated"}
    if new_sentence == 'SESSION_NOT_FOUND' or new_sentence == 'CARD_NOT_FOUND':
        return {"error":new_sentence.lower()}
    if new_sentence == 'ERROR':
        return {"error":"error_database"}
    return {"message":"sentence_created"}
    
def  update_sentence(id,session_id,text,order,image,audio,video,aux):
    if not isinstance(id,int):
        return {"error":"bad_id"}
    if not isinstance(session_id,int):
        return {"error":"bad_session_id"}
    up_sentence=db.update_sentence(id,session_id,text,order,image,audio,video,aux)
    if up_sentence == 'DUPLICATED':
        return {"error":"sentence_duplicated"}
    if up_sentence == 'BAD_ID':
        return {"error":"sentence_id_not_found"}
    if up_sentence != "SUCCESS":
        return {"error":"update_failed"}
    return {"message":"sentence_updated"}

def delete_sentence(id):
    if not isinstance(id,int):
        return {"error":"bad_sentence_id"}
    result = db.delete_sentence(id)
    if  result == 'ERROR':
        return {"error":"database_error"}
    if result == "USED_TOPIC":
        return {"error":"used_sentence"}
    return {"message":"sentence_deleted"}

def get_all_sentences():
    result=db.get_all_sentences()
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"sentences":[],"total":len(result)}
        for sentence in result:
            data["sentences"].append({"id":sentence[0],"session_id":sentence[1],"text":sentence[2],"order":sentence[3],"image":sentence[3],"audio":sentence[4],"video":sentence[5],"aux":sentence[6]})
        return data

def get_all_sentences_by_session(session_id):
    if not isinstance(session_id,int):
        return {"error":"bad_session_id"}
    result=db.get_sentences_by_session(session_id)
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"sentences":[],"total":len(result)}
        for sentence in result:
            data["sentences"].append({"id":sentence[0],"session_id":sentence[1],"text":sentence[2],"order":sentence[3],"image":sentence[3],"audio":sentence[4],"video":sentence[5],"aux":sentence[6]})
        return data
