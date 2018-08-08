import unittest
from onboarding import app, db, dirname

class BaseTest(unittest.TestCase):
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = u'sqlite:///' + dirname + u'/../test-onboard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.testing = True
    self.app = app.test_client()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
