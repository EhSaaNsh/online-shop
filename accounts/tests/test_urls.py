from django.test import TestCase, Client
from django.urls import reverse, resolve
from accounts.views import UserRegisterView, UserRegisterVerifyCodeView, UserLoginView, UserLogoutView


class TestUserRegister(TestCase):
    def test_register_url(self):
        url = reverse('accounts:user_register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)

    def test_verify_code_url(self):
        url = reverse('accounts:verify_code')
        self.assertEqual(resolve(url).func.view_class, UserRegisterVerifyCodeView)

    def test_login_url(self):
        url = reverse('accounts:user_login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_url(self):
        url = reverse('accounts:user_logout')
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)
