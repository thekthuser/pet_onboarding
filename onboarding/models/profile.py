from onboarding import db

class Profile(db.Model):
  __tablename__ = u'profiles'
  GENDERS = {u'MALE': u'Male', u'FEMALE': u'Female', u'UNSPECIFIED': u'Unspecified'}
  ACTIVITY_LEVEL = {u'SEDENTARY': u'Sedentary', u'LIGHT': u'Light',
    u'MODERATE': u'Moderate', u'HIGH': u'High', u'UNSPECIFIED': u'Unspecified'}
  BODY_LEVEL = {u'SKINNY': u'Skinny', u'IDEAL': u'Ideal', u'CHUBBY': u'Chubby', 
    u'UNSPECIFIED': u'Unspecified'}
  FOOD_TYPES = {u'DRY': u'Dry Food', u'WET': u'Wet Food', u'RAW': u'Raw Food', 
    u'FROZEN': u'Freeze Dried', u'HOME': u'Home Food', u'FRESH': u'Fresh Food', 
    u'UNSPECIFIED': u'Unspecified'}
  HUMAN_FOOD = {u'NEVER': u'Never', u'SOMETIMES': u'Sometimes', 
    u'ALWAYS': u'Always', u'UNSPECIFIED': u'Unspecified'}
  PRIMARY_PROTEIN = {u'LAMB': u'Lamb', u'TURKEY': u'Turkey', 
    u'CHICKEN': u'Chicken', u'BEEF': u'Beef', u'UNSPECIFIED': u'Unspecified'}
  DENTAL_CARE = {u'TREATS': u'Dental Treats', u'OTHER': u'Other Dental Care',
    u'NONE': u'None', u'UNSPECIFIED': u'Unspecified'}
  COAT_TYPES = {u'SHORT': u'Short-Coated', u'MEDIUM': u'Medium-Coated', 
    u'LONG': u'Long-Coated', u'WIRE': u'Wire-Coated', u'CURLY': u'Curly-Coated',
    u'HAIRLESS': u'Hairless', u'UNSPECIFIED': u'Unspecified'}
  OPTIONAL = [u'neutered', u'age', u'activity_level', u'weight', u'body_type', 
    u'food_types', u'human_food', u'protein', u'allergies', u'picky_eater', 
    u'dental', u'illnesses', u'medication', u'coat']

  id = db.Column(db.Integer, primary_key=True)
  owner_name = db.Column(db.Unicode(128), default=None, nullable=True)
  pet_name = db.Column(db.Unicode(128), default=None, nullable=True)
  zip_code = db.Column(db.Unicode(16), default=None, nullable=True)
  email = db.Column(db.Unicode(128), default=None, nullable=True)
  breed = db.Column(db.Unicode(64), default=None)
  gender = db.Column(db.Enum(*GENDERS.keys(), name=u'profile_genders', 
    validate_strings=True))
  neutered = db.Column(db.Boolean(), default=False)
  age = db.Column(db.Integer(), default=None)
  activity_level = db.Column(db.Enum(*ACTIVITY_LEVEL.keys(), validate_strings=True, 
    name=u'profile_activity'))
  weight = db.Column(db.Integer, default=None)
  body_type = db.Column(db.Enum(*BODY_LEVEL.keys(), name=u'profile_body', 
    validate_strings=True))
  #food_types is not an Enum, to handle multiple choices
  food_types = db.Column(db.Unicode(128), default=None)
  human_food = db.Column(db.Enum(*HUMAN_FOOD.keys(), name=u'profile_human', 
    validate_strings=True))
  protein = db.Column(db.Enum(*PRIMARY_PROTEIN.keys(), name=u'profile_protein', 
    validate_strings=True))
  allergies = db.Column(db.Unicode(256), default=None)
  picky_eater = db.Column(db.Boolean(), default=False)
  dental = db.Column(db.Enum(*DENTAL_CARE.keys(), name=u'profile_dental', 
    validate_strings=True))
  illnesses = db.Column(db.UnicodeText(), default=None)
  medication = db.Column(db.UnicodeText(), default=None)
  coat = db.Column(db.Enum(*COAT_TYPES.keys(), name=u'profile_coat', 
    validate_strings=True))
