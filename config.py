import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app): 
        pass

class DevelopmentConfig(Config):
    ENV='development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql+pymysql://root:@localhost/gestionImmodev'



class ProductionConfig(Config):
    ENV='production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL') or \
    'mysql+pymysql://root:@localhost/gestionImmoprod'

config = {
    'development': DevelopmentConfig,
   # 'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}