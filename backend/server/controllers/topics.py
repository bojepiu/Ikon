import database.topics as db


def create_topic(name):
    new_topic=db.insert_topic(name)
    if new_topic == 'DUPLICATED':
        return {"error":"topic_duplicated"}
    if new_topic == 'ERROR':
        return {"error":"error_database"}
    return {"message":"topic_created"}
    
def  update_topic(id,name):
    up_topic=db.update_topic(id,name)
    print(up_topic)
    if up_topic == 'DUPLICATED':
        return {"error":"topic_duplicated"}
    if up_topic != "SUCCESS":
        return {"error":"update_failed"}
    return {"message":"topic_updated"}

def delete_topic(id):
    if not isinstance(id,int):
        return {"error":"bad_topic_id"}
    result = db.delete_topic(id)
    if  result == 'ERROR':
        return {"error":"database_error"}
    if result == "USED_TOPIC":
        return {"error":"used_topic"}
    return {"message":"topic_deleted"}

def get_all_topics():
    result=db.get_all_topics()
    if result == "ERROR":
        return {"error":"error_database"}
    else:
        data={"topics":[],"total":len(result)}
        for topic in result:
            data["topics"].append({"id":topic[0],"name":topic[1]})
        return data

# print(create_topic('delete'))
# print(update_topic(4,'four_topic'))
# print(get_all_topics())
# print(delete_topic(2))
# print(get_all_topics())