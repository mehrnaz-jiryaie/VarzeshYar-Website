"""URLs for accounts app."""
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Login page
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Athlete registration page.
    path('register/', views.register_view, name='register'),
    # Successful registration
    path('register/successful-registration/',
         views.successful_registration, name='successful_registration'),
    # User profile
    path('profile/', views.profile_view, name='profile'),
    # Physical information page.
    path('profile/physical-information/', views.physical_information_view, name='physical-information'),
    # Trainaer registration page.
    path('trainer_register/', views.trainer_register_view, name='trainer_registeration'),
    # Trainaer login page.
    path('trainer_login/', views.trainer_login_view, name='login'),
]
