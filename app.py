from flask import Flask, render_template, send_from_directory
from services.user_services import my_users
from db import db 
from dotenv import load_dotenv
import os 
from config.mongo import mongo
from flask_smorest import Api


def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config['MONGO_URI']= os.getenv('MONGO_URI')
    mongo.init_app(app=app)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Api Flask Python"
    app.config["API_VERSION"] = "V1"

    #CONFIGURACION BDD
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "http://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)

    #creara las tablas de nuestra BDD
    #with app.app_context():
    #    db.create_all()

    api = Api(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/img/<string:name>')
    def send_img(name):
        return {
            "id": name
        }


    

    app.register_blueprint(my_users , url_prefix = "/my_users")

    return app

if __name__ == "__main__":
    create_app()