from app import create_app
from flask_script import Manager, Server
# from app.models import *


app = create_app('development')
manager=Manager(app)


manager.add_command('server',Server)
#this flask-script shell allows debugging is below
@manager.shell
def make_shell_context():
    return dict(app = app,)
#flask-script is above
if __name__ == '__main__':
    manager.run()