from flask import Blueprint
from security.token import token_required
from routes.topics import topic
from routes.user import user
from routes.cards import card

api = Blueprint('/api', __name__)
api.register_blueprint(topic,url_prefix='/topic')
api.register_blueprint(user,url_prefix='/user')
api.register_blueprint(card,url_prefix='/card')