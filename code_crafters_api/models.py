from django.db import models

# Create your models here.


class Recommendation(models.Model):
    description = models.TextField()
    date = models.DateField()
