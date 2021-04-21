from django.db import models

class ingredient(models.Model):
    name = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class tag(models.Model):
    name = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class recipe(models.Model):
    title = models.CharField(max_length = 50, unique=True)
    servings = models.PositiveSmallIntegerField()
    ingredients = models.ManyToManyField(ingredient, blank=True, through='ingredientAmount')
    description = models.TextField(max_length = 500)
    tags = models.ManyToManyField(tag, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class measure(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class ingredientAmount(models.Model):
    amount = models.FloatField()
    measure = models.ForeignKey(measure,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(recipe, on_delete=models.CASCADE)




