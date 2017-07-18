class DevConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://renato:1234@localhost:5432/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS =  True
    SQLALCHEMY_ECHO = True