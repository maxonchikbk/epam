from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = environ.get("POSTGRES_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False    