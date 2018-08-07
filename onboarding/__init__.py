import os
import pkg_resources
pkg_resources.require('Flask==1.0.2')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
dirname = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = u'sqlite:///' + dirname + u'/../onboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1UcSCEUgyOPKAUod'
app.config['DEBUG'] = True
csrf = CsrfProtect(app)
db = SQLAlchemy(app)

from services.web import register_web_endpoint
register_web_endpoint(app)
