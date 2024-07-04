from django.shortcuts import render
from accounts.models import TrainerAccount

def home(request):
    """Home Page"""
    return render(request, 'gym/home.html')

def trainers(request):
    """Shows list of all trainers."""
    trainers = TrainerAccount.objects.order_by('date_joined')
    return render(request, 'gym/trainers.html', {'trainers' : trainers})

def gyms_view(request):
    """Shows list of all gyms."""
    return render(request, 'gym/gyms.html')

def exc_list(request):
    """Shows list of all exercises."""
    return render(request, 'gym/exercises-list.html')