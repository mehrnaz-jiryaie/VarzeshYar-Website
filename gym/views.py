from django.shortcuts import render

def home(request):
    """Home Page"""
    return render(request, 'gym/home.html')

def trainers(request):
    """Shows list of all trainers."""
    return render(request, 'gym/trainers.html')

def gyms_view(request):
    """Shows list of all gyms."""
    return render(request, 'gym/gyms.html')