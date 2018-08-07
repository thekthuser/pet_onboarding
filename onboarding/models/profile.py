from onboarding import db

class Profile(db.Model):
  __tablename__ = u'profiles'
  id = db.Column(db.Integer, primary_key=True)
  owner_name = db.Column(db.Unicode(128), default=None)
