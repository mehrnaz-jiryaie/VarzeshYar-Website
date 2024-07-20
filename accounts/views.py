from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import AccountRegisterForm, LoginForm, ProfileForm, PhysicalInformationForm, TrainerRegisterForm, TrainerProfileForm, ProgramForm
from django.contrib.auth.decorators import login_required
from accounts.backends import AccountBackend, TrainerAccountBackend
from django.contrib.auth.forms import AuthenticationForm


def register_account_view(request):
    print('test1')
    if request.method == 'POST':
        print('test2')
        form = AccountRegisterForm(request.POST)
        print('test3')
        if form.is_valid():
            print('test4')
            user = form.save()
            print('test5')
            login(request, user, backend='accounts.backends.AccountBackend')
            print('test6')
            return redirect('accounts:successful_registration')
        else:
            print(form.errors) 
    else:
        print('test7')
        form = AccountRegisterForm()
        print('test8')
    return render(request, 'registration/register.html', {'form': form})


def register_trainer_account_view(request):
    if request.method == 'POST':
        form = TrainerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='accounts.backends.TrainerAccountBackend')
            return redirect('accounts:successful_registration')
    else:
        form = TrainerRegisterForm()
    return render(request, 'registration/trainer-register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password, backend='accounts.backends.AccountBackend')
            if user is not None:
                login(request, user, backend='accounts.backends.AccountBackend')
                return redirect('gym:home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def successful_registration(request):
    """Successful registration page."""
    return render(request, 'registration/successful_registration.html')


@login_required
def profile_view(request):
    print("Profile view accessed")
    # user = request.user
    # print(f"User: {user}")
    if request.method == 'POST':
        print("POST request received")
        form = ProfileForm(request.POST, instance=request.user, request=request)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('accounts:physical-information')
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        print("GET request received")
        form = ProfileForm(instance=request.user, request=request)
    return render(request, 'registration/profile.html', {'form': form})


@login_required
def physical_information_view(request):
    if request.method == 'POST':
        form = PhysicalInformationForm(request.POST, instance=request.user)
        if form.is_valid():
            print("Form2 is valid")
            form.save()
            return redirect('gym:home')
        else:
            print("Form2 is invalid")
            print(form.errors)
    else:
        form = PhysicalInformationForm(instance=request.user)
    return render(request, 'registration/physical_information.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('gym:home')



def trainer_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password, backend='accounts.backends.TrainerAccountBackend')
            if user is not None:
                login(request, user, backend='accounts.backends.TrainerAccountBackend')
                return redirect('gym:home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/trainer-login.html', {'form': form})


@login_required
def trainer_profile_view(request):
    if request.method == 'POST':
        form = TrainerProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('gym:home')
        
    else:
        form = TrainerProfileForm(instance=request.user)
    return render(request, 'registration/trainer-profile.html', {'form': form})


@login_required
def program_view(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('gym:home')
    else:
        form = ProgramForm(instance=request.user)
    return render(request, 'registration/sports-program.html', {'form':form})
