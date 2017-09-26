import flask
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, world'
