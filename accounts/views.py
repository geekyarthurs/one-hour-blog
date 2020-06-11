from django.shortcuts import render, redirect, reverse
from . import forms
from django.contrib.auth import authenticate, login, logout as lg
from django.views import View
from django.contrib.auth.models import User
# Create your views here.


class Signup(View):
    def get(self, request):
        form = forms.SignupForm()
        return render(request, "accounts/signup.html", {'form': form})

    def post(self, request):

        form = forms.SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('account:login')

        return render(request, "accounts/signup.html", {'form': form})


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "accounts/login.html", {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('blog:home')

        else:
            return render(request, "accounts/login.html", {'form': form})


def logout(request):
    lg(request)
    return redirect('account:login')
