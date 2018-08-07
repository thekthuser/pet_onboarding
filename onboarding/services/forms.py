from flask_wtf import Form
from wtforms import StringField, validators
from onboarding.models import Profile

class ProfileForm(Form):
  class Meta:
    model = Profile

  owner_name = StringField('Your name: ', [validators.DataRequired()])
