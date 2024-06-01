"""""URLs for gym app."""""
from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
]
