from django.db import models

# Create your models here.

# We define a model called 'Recommendation' that inherits from 'models.Model'.
class Recommendation(models.Model):
    description = models.TextField()
    date = models.DateField()
