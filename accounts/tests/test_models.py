from django.test import TestCase
from accounts.models import User
from model_bakery import baker


class TestUserModel(TestCase):
    def setUp(self):
        self.user = baker.make(User, email='abc@gmail.com')

    def test_str(self):
        self.assertEqual(str(self.user), 'abc@gmail.com')
