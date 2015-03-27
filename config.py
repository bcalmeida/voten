import os

# Default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xc7\xf6o5\xef\xf7c\xa7\x95gi\xbc\xf6<\xfaH7\xef\x9d\x98\xef\xdb\xe0\xfd'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

