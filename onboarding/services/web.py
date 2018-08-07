from onboarding.models import Profile
from flask import render_template

def register_web_endpoint(app):
  @app.route(u'/')
  def index():
    return render_template(u'profile_index.html')
