from flask import Blueprint,request,jsonify
from security.token import token_required,get_token

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