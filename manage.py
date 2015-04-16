from flask.ext.script import Manager

from config import config

from app import create_app, db

app = create_app('default')
manager = Manager(app)

if __name__ == '__main__':
    #app.run(host=config['server'])
    manager.run()
