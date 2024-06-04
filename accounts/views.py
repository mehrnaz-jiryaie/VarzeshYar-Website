from django.shortcuts import render, redirect
from .forms import AccountCreationForm, LoginForm, ProfileForm
from .models import *

        

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            # messages.success(request, 'Registration successful.')
            return redirect('accounts:successful_registration')
    else:
        form = AccountCreationForm()
        # context = {'form': form}
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    """Login page."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('gym:home')
    else:
        form = LoginForm()
    return render(request, 'registration\login.html', {'form': form})


def successful_registration(request):
    """Successful registration page."""
    return render(request, 'registration/successful.html')


def profile(request):
    """User profile page."""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            return redirect('registration:physical_information')
    else:
        form = ProfileForm()
    return render(request, 'registration/profile.html', {'form':form})


def physical_information(request):
    """Physical information page."""
    return render(request, 'registration/physical_information.html')