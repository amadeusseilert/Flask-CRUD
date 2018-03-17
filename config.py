class DevelopmentConfig(object):

    DEBUG = True
    SECRET_KEY = '\x1d\xeb-?\x8cHF\x18]r\x08\xf4\xf8\xcd\xe4\xa7\xe5^\xe2\xb5\x93\x8a\x93k'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(object):
    pass
