from flask import request,jsonify
from functools import wraps
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

#Initialized env vars
load_dotenv()

#Tiempo faltante requerido para solicitar el refresh del token
TIME_REFRESH_TOKEN=int(os.getenv('TIME_REFRESH_TOKEN'))
#Tiempo valido del token 
TIME_TOKEN = int(os.getenv('TIME_TOKEN'))


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, os.getenv("SECRET_KEY"))
            status=refresh_token(data)
            current_user=data
            if  status == 'ERROR' or status == 'EXPIRED':
                return jsonify({'message' : 'Invalid Token'}), 401
            if status != 'OK':
                current_user['new_token']=status
        except Exception as e:
            print(str(e))
            return jsonify({
                'message' : 'Invalid Token'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
    return decorated

def get_token(user,role):
    ##Validate user pwd
    token = jwt.encode({
        'role': role,
        'user': user,
        'exp' : datetime.utcnow() + timedelta(minutes = TIME_TOKEN)
    }, os.getenv('SECRET_KEY'))
    return token.decode('UTF-8')
    
def refresh_token(data):
    try:
        refresh=data['exp']
        user=data['user']
        role=data['role']
        if(datetime.utcfromtimestamp(refresh) < datetime.utcnow()):
            return "EXPIRED"
        if datetime.utcnow() + timedelta(minutes=TIME_REFRESH_TOKEN) > datetime.utcfromtimestamp(refresh):
            return jwt.encode({
                'role': role,
                'user': user,
                'exp' : datetime.utcnow() + timedelta(minutes = TIME_TOKEN)
            }, os.getenv('SECRET_KEY')).decode('UTF-8')
        else:
            print((datetime.utcfromtimestamp(refresh)) - (datetime.utcnow() + timedelta(minutes=TIME_REFRESH_TOKEN)) )
            return "OK"
    except Exception as e:
        print(str(e))
        return "ERROR"