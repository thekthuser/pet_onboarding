import pkg_resources
pkg_resources.require('Flask==1.0.2')
from flask import Flask

app = Flask(__name__)
