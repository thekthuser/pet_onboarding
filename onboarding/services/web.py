from onboarding.models import Profile, db
from onboarding.services.forms import ProfileForm
from flask import redirect, render_template, request, url_for


def register_web_endpoint(app):
  @app.route(u'/', methods=[u'GET', u'POST'])
  def index():
    form = ProfileForm(request.form)
    if request.method == u'POST' and form.validate():
      profile = Profile()
      existing = Profile.query.filter_by(email=form.email.data).all()
      if existing:
        for e in existing:
          if e.pet_name == form.pet_name.data:
            return u'This pet has already been registered.'
      if form.food_types.data:
        form.food_types.data = ','.join(form.food_types.data)
      else:
        form.food_types.data = None
      form.populate_obj(profile)
      db.session.add(profile)
      db.session.commit()
      return u'OK'
    return render_template(u'profile_index.html', form=form)

  @app.route(u'/view_profiles')
  def view_profiles():
    profiles = Profile.query.all()
    return render_template(u'profiles_view.html', profiles=profiles)
