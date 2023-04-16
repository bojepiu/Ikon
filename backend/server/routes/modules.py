from flask import Blueprint,request,jsonify
from security.token import token_required
from controllers import modules as ctl

#CONTEXT /module
module = Blueprint('/module', __name__)

@module.route('/get_all')
@token_required
def get_all_modules(data):
    try:
        result=ctl.get_all_modules()
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@module.route('/create',methods=["POST"])
@token_required
def create_module(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        name=js["name"]
        description=js["description"]
        result=ctl.create_module(name,description)
        if result.get('error'):
            if result["error"]=='module_duplicated':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})

@module.route("/update",methods=["POST"])
@token_required
def update_module(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        name=js["name"]
        id=js["id"]
        description=js["description"]
        result = ctl.update_module(id,name,description)
        if result.get('error'):
            if result["error"]=='module_duplicated':
                return jsonify(result),409
            elif result["error"]=="bad_id":
                return jsonify(result),400
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
    
@module.route("/delete",methods=["DELETE"])
@token_required
def delete_module(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        result = ctl.delete_module(id)
        print(result)
        if result.get('error'):
            if result["error"]=='used_module':
                return jsonify(result),409
            else:
                return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),204
        return jsonify(result),204
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)})
