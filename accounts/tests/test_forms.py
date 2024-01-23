from django.test import TestCase, Client
from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.models import User


class TestUserRegisterForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(phone_number='09121234578', email='abc@gmail.com', full_name='lorem ipsom', password='abcd')

    def test_valid_data(self):
        form = UserRegisterForm(data={'email': 'wer@gmail.com', 'full_name': 'mark hardi', 'phone': '09121234567', 'password': 'ABC'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_clean_email_method(self):
        form = UserRegisterForm(data={'email': 'abc@gmail.com', 'full_name': 'mark hardi', 'phone': '09121234567', 'password': 'ABC'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))

    def test_clean_phone_method(self):
        form = UserRegisterForm(data={'email': 'abcd@gmail.com', 'full_name': 'mark mark', 'phone': '09121234578', 'password': 'wsd'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('phone'))
