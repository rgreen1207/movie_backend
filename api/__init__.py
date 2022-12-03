import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/movie_flask.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Test!'
