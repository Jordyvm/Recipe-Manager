from django.db import models

class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)

     class Meta:
         abstract = True

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

class recipe(TimeStampedModel):
    title = models.CharField(max_length = 50, unique=True)
    coverImage = models.ImageField(max_length = 200)
    servings = models.PositiveSmallIntegerField()
    ingredients = models.ManyToManyField(ingredient, blank=True, through='ingredientAmount')
    description = models.TextField(max_length = 500)
    tags = models.ManyToManyField(tag, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_on']

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


