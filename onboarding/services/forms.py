from flask_wtf import Form
from wtforms import SelectField, StringField, validators
from wtforms.fields.html5 import EmailField
from onboarding.models import Profile

class ProfileForm(Form):
  class Meta:
    model = Profile

  owner_name = StringField('Your name: ', [validators.DataRequired()])
  pet_name = StringField('Your pet\'s name: ', [validators.DataRequired()])
  zip_code = StringField('Zipcode: ', [validators.DataRequired()])
  email = EmailField('Email: ', [validators.DataRequired(), validators.Email()])
  breed = StringField('Your pet\'s breed: ', [validators.DataRequired()])
  gender = SelectField('Your pet\'s gender: ', choices=zip(Profile.GENDERS.keys(), Profile.GENDERS.values()))
