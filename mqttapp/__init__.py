from logging.config import dictConfig
import flask
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, world'


def setup_logging():
    dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'std': {
                'format': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s] -- %(message)s',
                'datefmt': '%m-%d-%Y %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'std'
            },
        },
        'loggers': {
            'mqttapp': {
                'level': 'DEBUG',
                'handlers': ['console']
            },
        }
    })


setup_logging()
