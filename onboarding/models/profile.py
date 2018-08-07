from onboarding import db

class Profile(db.Model):
  __tablename__ = u'profiles'
  GENDERS = {u'MALE': u'Male', u'FEMALE': u'Female'}

  id = db.Column(db.Integer, primary_key=True)
  owner_name = db.Column(db.Unicode(128), default=None)
  pet_name = db.Column(db.Unicode(128), default=None)
  zip_code = db.Column(db.Unicode(16), default=None)
  email = db.Column(db.Unicode(128), default=None)
  breed = db.Column(db.Unicode(64), default=None)
  gender = db.Column(db.Enum(*GENDERS.values(), name=u'profile_genders'))
