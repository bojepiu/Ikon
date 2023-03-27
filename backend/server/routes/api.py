from flask import Blueprint

api = Blueprint('/api', __name__)

@api.route('/users')
def users():
    return "user"

@api.route('/posts')
def posts():
    return "post"