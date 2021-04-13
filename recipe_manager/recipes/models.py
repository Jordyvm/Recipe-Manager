from django.db import models

class ingredient(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class tag(models.Model):
    tag = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['tag']

class recipe(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    ingredients = models.ManyToManyField(ingredient, blank=True)
    tags = models.ManyToManyField(tag, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['title']



