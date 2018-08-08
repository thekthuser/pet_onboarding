from onboarding.tests.base import BaseTest
import unittest

class ProfileTests(BaseTest):
  def setUp(self):
    super(ProfileTests, self).setUp()

  def test_view_index(self):
    u"""
    Test index loads.
    """
    result = self.app.get(u'/')
    self.assertEqual(result.status_code, 200)
    self.assertIn(u'Pet Onboarding', result.data)
    self.assertIn(u'Please fill out this pet profile:', result.data)

if __name__ == '__main__':
  unittest.main()
