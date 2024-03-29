from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.

class UserTestCase(TestCase):
    def test_user(self):
        username = 'demo_user'
        password = 'admin@123'
        u = User(username=username)
        u.set_password(password)
        u.save()
        self.assertEqual(u.username, username)
        self.assertTrue(u.check_password(password))
