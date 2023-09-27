from django.db import models
from django.utils import timezone 

# Defines the model 'Recommendation' that inherits from 'models.Model'.
class Recommendation(models.Model):
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.description 
    
