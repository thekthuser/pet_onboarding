from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators
from wtforms.fields.html5 import EmailField
from onboarding.models import Profile

class ProfileForm(FlaskForm):
  class Meta:
    model = Profile
  def gender_validator(form, field):
    if field.data not in Profile.GENDERS.keys():
      raise validators.ValidationError(u'Please choose a gender.')

  owner_name = StringField(u'Your name: ', [validators.DataRequired()])
  pet_name = StringField(u'Your pet\'s name: ', [validators.DataRequired()])
  zip_code = StringField(u'Zipcode: ', [validators.DataRequired()])
  email = EmailField(u'Email: ', [validators.DataRequired(), validators.Email()])
  breed = StringField(u'Your pet\'s breed: ', [validators.Optional()])
  gender = SelectField(u'Your pet\'s gender: ', [gender_validator], 
    choices=zip(Profile.GENDERS.keys(), Profile.GENDERS.values()))
