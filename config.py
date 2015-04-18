
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://freeswitch:freeswitch@127.0.0.1/freeswitch"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'abc'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
        'default': DevelopmentConfig,
        'production': ProductionConfig,
        'server' : '0.0.0.0',
        'INFO' : 'INFO',
        'DEBUG' : 'DEBUG',
        'WARNING' : 'WARNING'
        }
