from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def recipes(request):
    return render(request, 'recipes.html')

def about(request):
    return render(request, 'about.html')