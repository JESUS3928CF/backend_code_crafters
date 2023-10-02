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




# Defines the model 'TypeInstitute'
class TypeInstitute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Defines the model 'EducationalInstitution'
class EducationalInstitution(models.Model):
    name = models.CharField(max_length=100)
    web_site = models.URLField(max_length=200, validators=[URLValidator()])
    id_type_institute = models.ForeignKey(TypeInstitute, on_delete=models.CASCADE)
    location = models.CharField(max_length=150, default="Colombia")
    #id_support = models.ForeignKey(Support, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Support(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    id_type_support = models.ForeignKey(TypeSupport, on_delete=models.CASCADE, default=1)
    url = models.URLField(max_length=200, validators=[URLValidator()])
    requirements = models.TextField(default="")
    #id_educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
class SupportForEducationalInstitution(models.Model):
    id_support = models.ForeignKey(Support, on_delete=models.CASCADE)
    id_educationalInstitution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE)

    
    
