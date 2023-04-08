from flask import Blueprint,request,jsonify
from security.token import token_required,get_token
from controllers import users as ctl

#CONTEXT /user
user = Blueprint('/user', __name__)

#ROUTES USER
@user.route('/login',methods=['POST'])
def users():
    try:
        j=request.get_json()
        user = j['user']
        pwd = j['password']
        result=ctl.validate_user(user,pwd)
        if result.get("error"):
            if result["error"]=="database_error":
                return jsonify(result),500
            else:
                return jsonify(result),403
        token=get_token(user,result["role"])
        if token != 'error':
            return jsonify({"message":"success","token":token}),200
        else:
            return jsonify({"error":"Bad Credentials"}),401
    except Exception as e:
        return jsonify({'error':'Bad Request',"exception":str(e)}),400
    
@user.route('/get_all',methods=["GET"])
@token_required
def get_all_users(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        result = ctl.get_all_users()
        if result.get('error'):
            return jsonify(result),500
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400

@user.route('/delete',methods=["DELETE"])
@token_required
def delete_user(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        j=request.get_json()
        id = j['id']
        result=ctl.delete_user(id)
        if result.get("error"):
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),204
        return jsonify(result),204
    except Exception as e:
        print(str(e))
        return jsonify({"error":"bad_request","exception":str(e)}),400

@user.route('/create',methods=["POST"])
@token_required
def create_user(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        userid=js['username']
        password=js['password']
        role=js['role']
        email=js["email"]
        result = ctl.create_user(userid,email,password,role)
        if result.get('error'):
            if result['error']=='error_database':
                return jsonify(result),500
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),201
        return jsonify(result),201
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400

@user.route('/update',methods=["POST"])
@token_required
def update_user(data):
    try:
        if data["role"] != 1:
            return jsonify({"error":"role_forbidden"}),403
        js=request.get_json()
        id=js["id"]
        userid=js['username']
        password=js['password']
        role=js['role']
        email=js["email"]
        result = ctl.update_user(id,userid,email,password,role)
        if result.get('error'):
            if result['error']=='error_database':
                return jsonify(result),500
            return jsonify(result),400
        if data.get('new_token'):
            result["new_token"]=data["new_token"]
            return jsonify(result),200 
        return jsonify(result),204
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400
