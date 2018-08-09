from onboarding.tests.base import BaseTest
from onboarding.models import Profile
import unittest

class ProfileTests(BaseTest):
  def setUp(self):
    super(ProfileTests, self).setUp()
    self.full_form = {u'owner_name': u'Chris', u'pet_name': u'TC', u'zip_code': u'11101', u'email': u'a@example.com', u'breed': u'Cat', u'gender': u'MALE', u'neutered': True, u'age': u'5', u'activity_level': u'LIGHT', u'weight': u'18', u'body_type': u'CHUBBY', u'food_types': u'', u'human_food': u'NEVER', u'protein': u'CHICKEN', u'allergies': u'', u'picky_eater': True, u'dental': u'NONE', u'illnesses': u'', u'medication': u'', u'coat': u'SHORT'}

  def test_view_index(self):
    u"""
    Test index loads.
    """
    result = self.app.get(u'/')
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'Pet Onboarding', result.data)
    self.assertIn(u'Please fill out this pet profile:', result.data)

  def test_missing_post(self):
    u"""
    Test POST with missing required fields.
    """
    result = self.app.post(u'/', data={u'owner_name': u'Chris', 
      u'pet_name': u'TC', u'email': u'a@example.com'})
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'Pet Onboarding', result.data)
    self.assertIn(u'Chris', result.data)
    self.assertIn(u'TC', result.data)
    self.assertIn(u'a@example.com', result.data)

    result = self.app.post(u'/', data={u'zip_code': u'11101'})
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'Pet Onboarding', result.data)
    self.assertIn(u'11101', result.data)
    self.assertNotIn(u'Chris', result.data)

  def test_full_post(self):
    u"""
    Test POST with all required fields, double submit, and db.
    """
    result = self.app.post(u'/', data=self.full_form, follow_redirects=True, content_type='application/x-www-form-urlencoded')
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'Your pet is now registered.', result.data)

    result = self.app.post(u'/', data=self.full_form, follow_redirects=True, content_type='application/x-www-form-urlencoded')
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'This pet has already been registered.', result.data)

  def test_post_db(self):
    u"""
    Test db status after POST.
    """
    result = self.app.post(u'/', data=self.full_form, follow_redirects=True, content_type='application/x-www-form-urlencoded')
    self.assertEqual(result.status_code, 200)

    profiles = Profile.query.all()
    self.assertEqual(len(profiles), 1)
    profile = profiles[0]
    self.assertEqual(profile.owner_name, u'Chris')
    self.assertEqual(profile.pet_name, u'TC')
    self.assertEqual(profile.zip_code, u'11101')
    self.assertEqual(profile.email, u'a@example.com')
    self.assertEqual(profile.breed, u'Cat')
    self.assertEqual(profile.gender, u'MALE')
    self.assertEqual(profile.neutered, True)
    self.assertEqual(profile.age, 5)
    self.assertEqual(profile.activity_level, u'LIGHT')
    self.assertEqual(profile.weight, 18)
    self.assertEqual(profile.body_type, u'CHUBBY')
    self.assertEqual(profile.food_types, u'')
    self.assertEqual(profile.human_food, u'NEVER')
    self.assertEqual(profile.protein, u'CHICKEN')
    self.assertEqual(profile.allergies, u'')
    self.assertEqual(profile.picky_eater, True)
    self.assertEqual(profile.dental, u'NONE')
    self.assertEqual(profile.illnesses, u'')
    self.assertEqual(profile.medication, u'')
    self.assertEqual(profile.coat, u'SHORT')

  def test_view_profiles(self):
    u"""
    Test view_profiles page.
    """
    result = self.app.post(u'/', data=self.full_form, follow_redirects=True, content_type='application/x-www-form-urlencoded')
    self.assertEqual(result.status_code, 200)

    result = self.app.get(u'/view_profiles')
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'Owner', result.data)
    self.assertIn(u'Chris', result.data)

if __name__ == '__main__':
  unittest.main()
