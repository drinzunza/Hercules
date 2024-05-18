from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignupForm, EditProfileForm
from .models import CustomUser
from django.contrib.auth import logout


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse('home')
    
def Logout(request):
    logout(request)
    return redirect('login')


class SignupView(CreateView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    
    def get_success_url(self):
        return reverse('login')
    
    
class EditProfile(UpdateView):
    model = CustomUser
    template_name= "users/edit_profile.html"
    form_class = EditProfileForm
    
    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse('feed')


def View_Profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render( request, "users/view_profile.html", {'profile':user})
