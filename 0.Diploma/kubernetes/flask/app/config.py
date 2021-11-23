from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = environ.get("POSTGRES_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    SECRET_KEY = b'BQ\x1aR\xb4_\x9c.\x15\xd0\xfa\xee\xff~\x01\x16'