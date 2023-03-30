from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

#ROUTES
from routes.api import  api
from routes.user import user

#INITIALIZED
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(user, url_prefix='/user')

@app.route("/")
def index():
    try:
        return jsonify({"message":"idnex"})
    except Exception as e:
        print(str(e))

@app.route("/about")
def aboutl():
    return  jsonify({"message":"about"})

if __name__ == '__main__':
    app.run(debug=True, 
         host='0.0.0.0', 
         port=os.getenv("PORT"))