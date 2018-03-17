class DevelopmentConfig(object):

    DEBUG = True
    TESTING = True
    SECRET_KEY = '\x1d\xeb-?\x8cHF\x18]r\x08\xf4\xf8\xcd\xe4\xa7\xe5^\xe2\xb5\x93\x8a\x93k'
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 5000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class ProductionConfig(object):
    DEBUG = False
    SECRET_KEY = '\x1d\xeb-?\x8cHF\x18]r\x08\xf4\xf8\xcd\xe4\xa7\xe5^\xe2\xb5\x93\x8a\x93k'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass
