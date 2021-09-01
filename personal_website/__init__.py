from flask import Flask 
from personal_website.config import Config
from personal_website.mainpages.routes import mainPages

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(mainPages)

    return app
