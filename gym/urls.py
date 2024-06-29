"""""URLs for gym app."""""
from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
    path('trainers/', views.trainers, name='trainers'),
    path('gyms/', views.gyms_view, name='gyms'),
    path('exc-list/',views.exc_list, name='exc-list'),
]
