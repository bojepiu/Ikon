from flask import Blueprint,request,jsonify
from security.token import token_required
from controllers import sessions as ctl

#CONTEXT /session
session = Blueprint('/session', __name__)

@session.route('/get_all')
@token_required
def get_all_sessions(data):
    try:
        result=ctl.get_all_sessions()
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@session.route('/get_by_module')
@token_required
def get_by_module(data):
    try:
        js=request.get_json()
        module_id=js['module_id']
        result=ctl.get_sessions_by_module(module_id)
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        if result.get("error"):
            if result["error"] == 'bad_module_id':
                return jsonify(result),400
            else:
                return jsonify(result),500
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@session.route('/create',methods=["POST"])
@token_required
def create_session(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        name=js["name"]
        module_id=js["module_id"]
        result=ctl.create_session(name,module_id)
        if result.get('error'):
            if result["error"]=='session_duplicated':
                return jsonify(result),409
            elif result["error"]=='module_id_not_found':
                return jsonify(result),400
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@session.route("/update",methods=["POST"])
@token_required
def update_session(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        name=js["name"]
        module_id=js["module_id"]
        id=js["id"]
        result = ctl.update_session(id,module_id,name)
        if result.get('error'):
            if result["error"]=='session_duplicated':
                return jsonify(result),409
            elif result["error"]=="bad_id" or result["error"]=='bad_module_id':
                return jsonify(result),400
            elif result["error"]== 'id_not_found' or result["error"]== 'module_id_not_found':
                return jsonify(result),400
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
    
@session.route("/delete",methods=["DELETE"])
@token_required
def delete_session(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        result = ctl.delete_session(id)
        print(result)
        if result.get('error'):
            if result["error"]=='used_session':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),204
        return jsonify(result),204
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
