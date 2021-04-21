from django.contrib import admin

from .models import ingredient, recipe, tag, ingredientAmount, measure

admin.site.register(ingredient)
admin.site.register(measure)
# admin.site.register(recipe)
admin.site.register(tag)

# @admin.register(ingredientAmount)
class ingredientAmountInline(admin.TabularInline):
    model = ingredientAmount
    extra = 1

# @admin.register(ingredient)
# class ingredientAdmin(admin.ModelAdmin):
#     inlines = (ingredientAmountInline,)

@admin.register(recipe)
class recipeAdmin(admin.ModelAdmin):
    inlines = (ingredientAmountInline,)

