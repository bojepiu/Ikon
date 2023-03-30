from flask import Blueprint
from security.token import token_required

api = Blueprint('/api', __name__)
@token_required
@api.route('/users')
def users():
    return "user"

@api.route('/posts')
@token_required
def posts():
    return "post"