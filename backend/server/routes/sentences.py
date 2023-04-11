from flask import Blueprint,request,jsonify
from security.token import token_required
from controllers import sentences as ctl

#CONTEXT /card
sentence = Blueprint('/sentence', __name__)

@sentence.route('/get_all',methods=["GET"])
@token_required
def get_all_sentences(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        result=ctl.get_all_sentences()
        if result.get('error'):
            return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400

@sentence.route('/get_by_session',methods=["GET"])
@token_required
def get_all_sentences_by_session(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        session_id=js["session_id"]
        result=ctl.get_all_sentences_by_session(session_id)
        if result.get('error'):
            if result['error'] == "error_database":
                return jsonify(result),500
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400

@sentence.route('/create',methods=["POST"])
@token_required
def create_sentence(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        session_id=js["session_id"]
        text=js["text"]
        order=js["order"]
        image=js["image"]
        audio=js["audio"]
        video=js["video"]
        aux=js["aux"]
        result=ctl.create_sentence(session_id,text,order,image,audio,video,aux)
        if result.get('error'):
            if result["error"] == "error_database":
                return jsonify(result),500
            if result["error"] == "sentence_duplicated":
                return jsonify(result),409
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400

@sentence.route('/update',methods=["POST"])
@token_required
def update_sentence(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        session_id=js["session_id"]
        text=js["text"]
        order=js["order"]
        image=js["image"]
        audio=js["audio"]
        video=js["video"]
        aux=js["aux"]
        result=ctl.update_sentence(id,session_id,text,order,image,audio,video,aux)
        if result.get('error'):
            if result["error"] == "error_database":
                return jsonify(result),500
            if result["error"] == "sentence_duplicated":
                return jsonify(result),409
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400

@sentence.route('/delete',methods=["DELETE"])
@token_required
def delete_sentence(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        result=ctl.delete_sentence(id)
        if result.get('error'):
            if result['error'] == "error_database":
                return jsonify(result),500
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400
