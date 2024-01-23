from django.test import TestCase, Client
from django.urls import resolve, reverse
from accounts.forms import UserRegisterForm, VerifyCodeForm
from accounts.models import User


class TestUserRegisterView(TestCase):
    def setUp(self):
        self.client = Client()


    def test_user_register_GET(self):
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.failUnless(response.context['form'], UserRegisterForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('accounts:user_register'), data={'email': 'test@gmail.com', 'full_name': 'abcdef', 'phone':'09141234567', 'password':'qwer'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:verify_code'))

    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse('accounts:user_register'), data={'email': 'test_gmail.com', 'full_name': 'abcdef', 'phone':'09141234567', 'password':'qwer'})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(form=response.context['form'], field='email', errors=['Enter a valid email address.'])


class TestUserRegisterVerifyCode(TestCase):

    def setUp(self):
        self.client = Client()

    def test_verify_code_GET(self):
        response = self.client.get(reverse('accounts:verify_code'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/verify.html')
        self.failUnless(response.context['form'], VerifyCodeForm)



