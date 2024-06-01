from django.shortcuts import render

def home(request):
    "Home Page"
    return render(request, 'gym/home.html')

def trainers(request):
    "Shows a list of all trainers."
    return render(request, 'gym/trainers.html')
