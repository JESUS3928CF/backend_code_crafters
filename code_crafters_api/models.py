from django.db import models
from django.utils import timezone 
from django.core.validators import URLValidator

# Defines the model 'Recommendation' that inherits from 'models.Model'.
class Recommendation(models.Model):
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.description 


# Defines the model 'TypeSupport'
class TypeSupport(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.name 

# Defines the model 'Support'

class Support(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    type_support = models.ForeignKey(TypeSupport, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, validators=[URLValidator()])
    requirements = models.TextField()

    def __str__(self):
        return self.name




    
