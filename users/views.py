from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('home')
