from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:successful_registration')
        else:
            # Print form errors for debugging
            print("Form errors: ", form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('gym:home')
        else:
            print("Form errors: ", form.errors)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



def successful_registration(request):
    """Successful registration page."""
    return render(request, 'registration/successful.html')


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

# @login_required
# def physical_information(request):
#     """Physical information page."""
#     if request.method == 'POST':
#         form = PhysicalInformationForm(request.POST)
#         if form.is_valid():
#             return redirect('gym:home')
#     else:
#         form = PhysicalInformationForm()
#     return render(request, 'registration/physical_information.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('gym:home')