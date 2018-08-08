from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, SelectMultipleField, StringField, validators
from wtforms.fields.html5 import EmailField
from onboarding.models import Profile

class ProfileForm(FlaskForm):
  class Meta:
    model = Profile
  def gender_validator(form, field):
    if field.data not in Profile.GENDERS.keys():
      raise validators.ValidationError(u'Please choose a gender.')
  def activity_validator(form, field):
    if field.data not in Profile.ACTIVITY_LEVEL.keys():
      raise validators.ValidationError(u'Please choose an activity level.')
  def body_validator(form, field):
    if field.data not in Profile.BODY_LEVEL.keys():
      raise validators.ValidationError(u'Please choose an body type.')
  def food_validator(form, field):
    if field.data not in Profile.FOOD_TYPES.keys():
      raise validators.ValidationError(u'Please choose all food types.')
  def protein_validator(form, field):
    if field.data not in Profile.PRIMARY_PROTEIN.keys():
      raise validators.ValidationError(u'Please choose a primary protein.')
  def dental_validator(form, field):
    if field.data not in Profile.DENTAL_CARE.keys():
      raise validators.ValidationError(u'Please choose a dental care routine.')
  def coat_validator(form, field):
    if field.data not in Profile.COAT_TYPES.keys():
      raise validators.ValidationError(u'Please choose a coat type.')

  owner_name = StringField(u'Your name: ', [validators.DataRequired()])
  pet_name = StringField(u'Your pet\'s name: ', [validators.DataRequired()])
  zip_code = StringField(u'Zipcode: ', [validators.DataRequired()])
  email = EmailField(u'Email: ', [validators.DataRequired(), validators.Email()])
  breed = StringField(u'Your pet\'s breed: ', [validators.Optional()])
  gender = SelectField(u'Your pet\'s gender: ', [gender_validator], 
    choices=zip(Profile.GENDERS.keys(), Profile.GENDERS.values()))
  neutered = BooleanField(u'Neutered: ')
  age = IntegerField(u'Age: ', [validators.Optional()])
  activity_level = SelectField(u'Activity level: ', [activity_validator, validators.Optional()],
    choices=zip(Profile.ACTIVITY_LEVEL.keys(), Profile.ACTIVITY_LEVEL.values()))
  weight = IntegerField(u'Weight: ', [validators.Optional()])
  body_type = SelectField(u'Body type: ', [body_validator, validators.Optional()],
    choices=zip(Profile.BODY_LEVEL.keys(), Profile.BODY_LEVEL.values()))
  food_types = SelectMultipleField(u'Food types: ', [food_validator, validators.Optional()],
    choices=zip(Profile.FOOD_TYPES.keys(), Profile.FOOD_TYPES.values()))
  protein = SelectField(u'Primary protein: ', [protein_validator, validators.Optional()],
    choices=zip(Profile.PRIMARY_PROTEIN.keys(), Profile.PRIMARY_PROTEIN.values()))
  allergies = StringField(u'Allergies: ')
  picky_eater = BooleanField(u'Picky eater: ')
  dental = SelectField(u'Dental care: ', [dental_validator, validators.Optional()],
    choices=zip(Profile.DENTAL_CARE.keys(), Profile.DENTAL_CARE.values()))
  illnesses = StringField(u'Illnesses: ')
  medication = StringField(u'Medications: ')
  coat = SelectField(u'Coat type: ', [coat_validator, validators.Optional()],
    choices=zip(Profile.COAT_TYPES.keys(), Profile.COAT_TYPES.values()))
