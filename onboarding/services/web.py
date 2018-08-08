from onboarding.models import Profile, db
from onboarding.services.forms import ProfileForm
from flask import redirect, render_template, request, url_for

from flask_wtf import Form
from flask_wtf import FlaskForm
#from wtforms.ext.appengine.db import model_form
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms import validators


def register_web_endpoint(app):
  @app.route(u'/', methods=['GET', 'POST'])
  def index():
    form = ProfileForm(request.form)
    if request.method == 'POST' and form.validate():
      profile = Profile()
      form.populate_obj(profile)
      db.session.add(profile)
      db.session.commit()
      return 'OK'
    return render_template(u'profile_index.html', form=form)

  @app.route(u'/view_profiles')
  def view_profiles():
    profiles = Profile.query.all()
    return render_template('profiles_view.html', profiles=profiles)
