from django.urls import path
from .views import CustomLoginView, SignupView, View_Profile, Logout, EditProfile

urlpatterns = [
    path('auth/login', CustomLoginView.as_view(), name='login'),
    path('auth/signup', SignupView.as_view(), name='signup'),
    path('users/edit_profile', EditProfile.as_view(), name='edit_profile'),
    path('auth/logout', Logout, name='logout'),
    path('user/view_profile/<int:user_id>', View_Profile, name="view_profile"),
]

