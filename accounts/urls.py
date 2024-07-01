"""URLs for accounts app."""
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Athlete login page
    # path('login/', views.login_view, name='athlete-login'),
    # Log out page
    path('logout/', views.logout_view, name='logout'),
    # Athlete registration page.
    path('register/', views.register_account_view, name='register'),
    # Successful registration
    path('register/successful-registration/',
         views.successful_registration, name='successful_registration'),
    # Athlete profile
    path('profile/', views.profile_view, name='profile'),
    # Physical information page.
    path('profile/physical-information/', views.physical_information_view, name='physical-information'),
    # Trainer registration page.
    path('trainer_register/', views.register_trainer_account_view, name='trainer_registeration'),
    # Trainer login page.
    path('trainer_login/', views.trainer_login_view, name='trainer-login'),
    # Trainer profile page.
    path('trainer_profile/', views.trainer_profile_view, name='trainer_profile'),
    # Athlete login page
    path('login/account/', views.login_view, name='athlete-login'),
    # Trainer login page
    path('login/trainer_account/', views.trainer_login_view, name='trainer-login'),
    # Exercise program page
    path('profile/program/', views.program_view, name='exc-program'),
]
