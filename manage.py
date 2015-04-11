from config import config

from app import create_app, db

app = create_app('default')


if __name__ == '__main__':
    app.run(host=config['server'])
