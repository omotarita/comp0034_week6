"""Flask config class."""
import pathlib


class Config(object):
    '''
    This is a teaching instruction and not a docstring for the function!

    Try the following code in a Python console to generate your own secret key and then past it below where it
    currently says 'generate_a_secret_key'. This uses secrets: https://docs.python.org/3/library/secrets.html

    import secrets

    print(secrets.token_urlsafe(16))
    '''
    # SECRET_KEY = 'generate_a_secret_key'
    SECRET_KEY = 'M36QAHl1m6BJE9UZr0MUBQ'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent.joinpath('lab_example.sqlite'))


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = True
