from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap

def create_app(config_name):
    app=Flask(__name__)
    from .main import main as main_blueprint
    
    bootstrap.init_app('self',app)
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app