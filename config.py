
class Config:

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
