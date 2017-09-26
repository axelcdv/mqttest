import os


DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

CLOUDMQTT_URL = 'localhost'
