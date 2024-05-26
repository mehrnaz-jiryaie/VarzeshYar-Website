from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import AccountCreationForm, LoginForm
from django.contrib import messages

# from rest_framework import viewsets, permissions
# from .serializers import *
# from rest_framework.response import Response
from .models import *

# class AccountViewset(viewsets.ViewSet):
    # permission_classes = [permissions.AllowAny]
    # queryset = Account.objects.all()
    # serializer_class = AccountSerializer

    # def list(self, request):
    #     queryset = Account.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)

    # def retrieve(self, request, pk=None):
    #     account = Account.objects.get(pk=pk)
    #     serializer = self.serializer_class(account)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     account = Account.objects.get(pk=pk)
    #     serializer = self.serializer_class(account, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)

    # def destroy(self, request, pk=None):
    #     account = Account.objects.get(pk=pk)
    #     account.delete()
    #     return Response(status=204)
        

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            form.save()
            # login(request, user)
            # messages.success(request, 'Registration successful.')
            return redirect('gym:index')
    else:
        form = AccountCreationForm()
        # context = {'form': form}
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    """Login page."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gym:index')
    else:
        form = LoginForm()
    return render(request, 'registration\login.html', {'form':'form'})


def successful_registration(request):
    """Successful registration page."""
    return render(request, 'registration/Successful_registration.html')