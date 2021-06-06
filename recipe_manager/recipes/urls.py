from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeRecipes, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('about/', views.about, name='about'),
]