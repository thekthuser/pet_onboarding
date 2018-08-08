from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, SelectMultipleField, StringField, validators
from wtforms.fields.html5 import EmailField
from onboarding.models import Profile

class ProfileForm(FlaskForm):
  class Meta:
    model = Profile
  def food_validator(form, field):
    for f in field.data:
      if f not in Profile.FOOD_TYPES.keys():
        raise validators.ValidationError(u'Please choose some food types.')

  owner_name = StringField(u'Your name: ', [validators.DataRequired()])
  pet_name = StringField(u'Your pet\'s name: ', [validators.DataRequired()])
  zip_code = StringField(u'Zipcode: ', [validators.DataRequired()])
  email = EmailField(u'Email: ', [validators.DataRequired(), validators.Email()])
  breed = StringField(u'Your pet\'s breed: ', [validators.Optional()])
  gender = SelectField(u'Your pet\'s gender: ', 
    choices=zip(Profile.GENDERS.keys(), Profile.GENDERS.values()))
  neutered = BooleanField(u'Neutered: ')
  age = IntegerField(u'Age: ', [validators.Optional()])
  activity_level = SelectField(u'Activity level: ', [validators.Optional()],
    choices=zip(Profile.ACTIVITY_LEVEL.keys(), Profile.ACTIVITY_LEVEL.values()))
  weight = IntegerField(u'Weight: ', [validators.Optional()])
  body_type = SelectField(u'Body type: ', [validators.Optional()],
    choices=zip(Profile.BODY_LEVEL.keys(), Profile.BODY_LEVEL.values()))
  food_types = SelectMultipleField(u'Food types: ', [food_validator, validators.Optional()],
    choices=zip(Profile.FOOD_TYPES.keys(), Profile.FOOD_TYPES.values()))
  human_food = SelectField(u'Eats human food: ', [validators.Optional()],
    choices=zip(Profile.HUMAN_FOOD.keys(), Profile.HUMAN_FOOD.values()))
  protein = SelectField(u'Primary protein: ', [validators.Optional()],
    choices=zip(Profile.PRIMARY_PROTEIN.keys(), Profile.PRIMARY_PROTEIN.values()))
  allergies = StringField(u'Allergies: ')
  picky_eater = BooleanField(u'Picky eater: ')
  dental = SelectField(u'Dental care: ', [validators.Optional()],
    choices=zip(Profile.DENTAL_CARE.keys(), Profile.DENTAL_CARE.values()))
  illnesses = StringField(u'Illnesses: ')
  medication = StringField(u'Medications: ')
  coat = SelectField(u'Coat type: ', [validators.Optional()],
    choices=zip(Profile.COAT_TYPES.keys(), Profile.COAT_TYPES.values()))
