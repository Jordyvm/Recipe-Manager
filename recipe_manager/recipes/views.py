from django.shortcuts import render
from django.http import HttpResponse
from .models import recipe

def home(request):
    return render(request, 'home.html')

def recipes(request):
    allRecipes = recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': allRecipes})

def about(request):
    return render(request, 'about.html')

def homeRecipes(request):
    allRecipes = recipe.objects.all()
    return render(request, 'home.html', {'recipes': allRecipes})
