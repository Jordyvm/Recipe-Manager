from django.contrib import admin

from .models import ingredient, recipe, tag

admin.site.register(ingredient)
admin.site.register(recipe)
admin.site.register(tag)