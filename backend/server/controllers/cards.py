import database.cards as db
HTTP='http'

def get_all_cards():
    result=db.get_all_cards()
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"cards":[],"total":len(result)}
        for topic in result:
            data["cards"].append({"id":topic[0],"topic_id":topic[1],"text":topic[2],"image":topic[3],"audio":topic[4],"video":topic[5],"aux":topic[6]})
        return data


def create_card(topic_id,text,image,audio,video,aux):
    if not isinstance(topic_id,int):
        return {"error":"bad_topicid"}
    #PENDING VALIDATE RESOURCES
    # if not image.includes(HTTP):
    #     return {"error":"bad_image"}
    new_card=db.insert_card(topic_id,text,image,audio,video,aux)
    if new_card == 'DUPLICATED':
        return {"error":"card_duplicated"}
    if new_card == 'ERROR':
        return {"error":"error_database"}
    return {"message":"card_created"}
    
def  update_card(id,topic_id,text,image,audio,video,aux):
    if not isinstance(id,int):
        return {"error":"bad_id"}
    if not isinstance(topic_id,int):
        return {"error":"bad_topicid"}
    if text == '':
        return {"error":"bad_text"}
    if image == '':
        return {"error":"bad_image"}
    up_card=db.update_card(id,topic_id,text,image,audio,video,aux)
    print(up_card)
    if up_card == 'DUPLICATED':
        return {"error":"card_duplicated"}
    if up_card == 'TOPIC_NOT_FOUND':
        return {"error":up_card.lower()}
    if up_card != "SUCCESS":
        return {"error":"update_failed"}
    return {"message":"card_updated"}

def delete_card(id):
    if not isinstance(id,int):
        return {"error":"bad_card_id"}
    result = db.delete_card(id)
    if  result == 'ERROR':
        return {"error":"database_error"}
    if result == "USED":
        return {"error":"used_card"}
    return {"message":"card_deleted"}


def get_all_cards_by_topic(topic_id):
    if not isinstance(topic_id,int):
        return {"error":"bad_topic_id"}
    result=db.get_cards_by_topic(topic_id)
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"cards":[],"total":len(result)}
        for topic in result:
            data["cards"].append({"id":topic[0],"topic_id":topic[1],"text":topic[2],"image":topic[3],"audio":topic[4],"video":topic[5],"aux":topic[6]})
        return data

# print(create_card('delete'))
# print(update_card(4,'four_topic'))
# print(get_all_cards())
# print(delete_card(2))
# print(get_all_cards_by_topic())