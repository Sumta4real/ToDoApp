import os
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

# Create your tests here.
class TryDjangoConfigTest(TestCase):
    #create method to test the strength of the secret key
    def test_secret_key_srength(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak Secret Key {e.messages}'
            self.fail(msg)
        #self.assertTrue(1==1)

