from flask import Blueprint,request,jsonify
from security.token import token_required
from controllers import topics as ctl

#CONTEXT /topic
topic = Blueprint('/topic', __name__)

@topic.route('/get_all')
@token_required
def get_all_topics(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        result=ctl.get_all_topics()
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@topic.route('/create',methods=["POST"])
@token_required
def create_topic(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        name=js["name"]
        result=ctl.create_topic(name)
        if result.get('error'):
            if result["error"]=='topic_duplicated':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@topic.route("/update",methods=["POST"])
@token_required
def update_topic(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        name=js["name"]
        id=js["id"]
        result = ctl.update_topic(id,name)
        if result.get('error'):
            if result["error"]=='topic_duplicated':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
    
@topic.route("/delete",methods=["DELETE"])
@token_required
def delete_topic(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        result = ctl.delete_topic(id)
        print(result)
        if result.get('error'):
            if result["error"]=='used_topic':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),204
        return jsonify(result),204
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
