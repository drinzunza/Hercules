from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import SignupForm
from .models import CustomUser


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('home')


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm

    def get_success_url(self):
        return reverse('login')


def View_Profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, "users/view_profile.html", {'user': user})