from onboarding import CsrfProtect, csrf
from onboarding.models import Profile, db
from onboarding.services.forms import ProfileForm
from flask import redirect, render_template, url_for

def register_web_endpoint(app):
  @app.route(u'/')
  def index():
    form = ProfileForm()
    return render_template(u'profile_index.html', form=form)

  @app.route(u'/edit_profile', methods=['POST'])
  def edit_profile():
    form = ProfileForm()
    if form.validate():
      profile = Profile(owner_name=form.owner_name.data, 
        pet_name=form.pet_name.data, zip_code=form.zip_code.data, 
        email=form.email.data, breed=form.breed.data, gender=form.gender.data)
      db.session.add(profile)
      db.session.commit()
      return 'OK'
    return redirect(url_for('index'))

  @app.route(u'/view_profiles')
  def view_profiles():
    profiles = Profile.query.all()
    return render_template('profiles_view.html', profiles=profiles)
