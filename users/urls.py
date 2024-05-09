from django.urls import path
from .views import CustomLoginView, SignupView, View_Profile

urlpatterns = [
    path('auth/login', CustomLoginView.as_view(), name="login"),
    path('auth/signup', SignupView.as_view(), name='signup'),
    path('users/view_profile/<int:user_id>', View_Profile, name="view_profile")
]

