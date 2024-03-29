from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from flask_login import LoginManager #loggin

bootstrap=Bootstrap
# login_manager = LoginManager() # allows login
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

def create_app(config_name):
    app=Flask(__name__)
    from .main import main as main_blueprint
    bootstrap.init_app('self',app)
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app