from django.views import View
from .forms import UserRegisterForm, VerifyCodeForm, UserLoginForm
from django.shortcuts import render,redirect
import random
from django.contrib import messages
from utils import send_otp_code
from . models import OtpCode, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
import pytz



class UserRegisterView(View):
    form_class = UserRegisterForm
    template_class = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_class, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = 2545 ## chon service payamak nadaram
            #random_code = random.randint(1000, 9999)
            #send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password']
            }
            messages.success(request, 'verify code sent', 'success')
            return redirect('accounts:verify_code')
        return render(request, self.template_class, {'form': form})


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        user_session = request.session['user_registration_info']
        expire_otp_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=1)
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code and not code_instance.created < expire_otp_time:
                User.objects.create_user(phone_number=user_session['phone_number'], email=user_session['email'],
                                         full_name=user_session['full_name'], password=user_session['password'])
                code_instance.delete()
                messages.success(request, 'you are registered successfully', 'success')
                return redirect('home:home')
            messages.error(request, 'this code in not valid', 'danger')
            return redirect('accounts:verify_code')
        return render(request, 'accounts/verify.html', {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_class = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_class, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you are logged in', 'success')
                return redirect('home:home')
            messages.error(request, 'phone or password is wrong', 'warning')
            return redirect('home:home')
        return render(request, self.template_class, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')
