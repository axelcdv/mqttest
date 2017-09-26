import os


DEBUG = True

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgres://lancelot@localhost/uptime_iotpad'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
