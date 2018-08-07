import os
import pkg_resources
pkg_resources.require('Flask==1.0.2')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dirname = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dirname + '/../onboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)

from services.web import register_web_endpoint
register_web_endpoint(app)
