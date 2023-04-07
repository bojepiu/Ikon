from flask import Blueprint,request,jsonify
from security.token import token_required,get_token
from controllers import users as ctl

#CONTEXT /user
user = Blueprint('/user', __name__)

#ROUTES
@user.route('/login',methods=['POST'])
def users():
    try:
        j=request.get_json()
        user = j['user']
        pwd = j['pwd']
        token=get_token(user,pwd)
        if token != 'error':
            return jsonify({"message":"success","token":token}),200
        else:
            return jsonify({"error":"Bad Credentials"}),401
    except Exception as e:
        return {'error':'Bad Request',"e":str(e)},400

@user.route('/logout')
@token_required
def logout(data):
    return data,200

@user.route('/create_user',methods=["POST"])
@token_required
def create_user(data):
    try:
        print(data)
        js=request.get_json()
        print(js)
        userid=js['username']
        password=js['password']
        role=js['role']
        email=js["email"]
        result = ctl.create_user(userid,email,password,role)
        if result.get('error'):
            if result['error']=='error_database':
                return jsonify(result),500
            return jsonify(result),400
        return jsonify(result),201
    except Exception as e:
        return jsonify({"error":"bad_request","exception":str(e)}),400