from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/notes')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'today': datetime.today()}
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['today'] = datetime.today()
    #     return context


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/login'


