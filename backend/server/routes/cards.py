from flask import Blueprint,request,jsonify
from security.token import token_required
from controllers import cards as ctl

#CONTEXT /card
card = Blueprint('/card', __name__)

@card.route('/get_all')
@token_required
def get_all_cards(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        result=ctl.get_all_cards()
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@card.route('/create',methods=["POST"])
@token_required
def create_card(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        topic_id=js["topic_id"]
        text=js["text"]
        image=js["image"]
        audio=js["audio"]
        video=js["video"]
        aux=js["aux"]
        result=ctl.create_card(topic_id,text,image,audio,video,aux)
        if result.get('error'):
            if result["error"]=='card_duplicated':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@card.route("/update",methods=["POST"])
@token_required
def update_card(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        topic_id=js["topic_id"]
        text=js["text"]
        image=js["image"]
        audio=js["audio"]
        video=js["video"]
        aux=js["aux"]
        result = ctl.update_card(id,topic_id,text,image,audio,video,aux)
        if result.get('error'):
            if result["error"]=='update_failed':
                return jsonify(result),500
            elif result["error"]=='card_duplicated':
                 return jsonify(result),409
            else:
                return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
    
@card.route("/delete",methods=["DELETE"])
@token_required
def delete_card(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        result = ctl.delete_card(id)
        print(result)
        if result.get('error'):
            if result["error"]=='used_card':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),204
        return jsonify(result),204
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
