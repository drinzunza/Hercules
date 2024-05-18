from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username')
        
        
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'status','email', 'first_name', 'last_name', 'birthday',
    'phone_number', 'locatoin', 'bio', 'color', 'profile_picture'
        ]
        
        
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }