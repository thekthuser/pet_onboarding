from onboarding import CsrfProtect, csrf
from onboarding.models import Profile
from onboarding.services.forms import ProfileForm
from flask import render_template

def register_web_endpoint(app):
  @app.route(u'/')
  def index():
    form = ProfileForm()
    return render_template(u'profile_index.html', form=form)

  @app.route(u'/edit_profile', methods=['POST'])
  def edit_profile():
   return 'POST form' 
