from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=200)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    birthday = models.DateField(null=True, blank=True)
    join_date = models.DateField(default=datetime.now)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to="media/profile/", null=True, blank=True)
    locatoin = models.CharField(max_length=200 , blank=True)
    bio = models.TextField(blank=True)
    status = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=30, blank=True)
    
    objects = CustomUserManager()
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    