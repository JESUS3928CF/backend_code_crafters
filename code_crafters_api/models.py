from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from django.core.validators import URLValidator

# Defines the model 'Recommendation' that inherits from 'models.Model'.
class Recommendation(models.Model):
    description = models.TextField(_("Description"))
    date = models.DateField(_("Date"), default=timezone.now)

    class Meta:
        verbose_name = _("Recomendation")
        verbose_name_plural = _("Recomendations")

    def __str__(self):
        return self.description 

# Defines the model 'TypeSupport'
class TypeSupport(models.Model):
    name = models.CharField(_("Name"), max_length=75)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = _("Type support")
        verbose_name_plural = _("Type supports")

    def __str__(self):
        return self.name 

# Defines the model 'TypeInstitute'
class TypeInstitute(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    description = models.TextField(_("Descripción"))

    class Meta:
        verbose_name = _("Type institution")
        verbose_name_plural = _("Type institutions")

    def __str__(self):
        return self.name

# Defines the model 'EducationalInstitution'
class EducationalInstitution(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    web_site = models.URLField(_("Web site"), max_length=200, validators=[URLValidator()])
    id_type_institute = models.ForeignKey(TypeInstitute, on_delete=models.CASCADE, verbose_name=_("Type Institution"))
    location = models.CharField(_("Location"), max_length=150, default="Colombia")
    #id_support = models.ForeignKey(Support, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Educational institution")
        verbose_name_plural = _("Educational institutions")

    def __str__(self):
        return self.name
    
# Defines the model 'Support'
class Support(models.Model):
    name = models.CharField(_("Name"), max_length=75)
    description = models.TextField(_("Description"))
    id_type_support = models.ForeignKey(TypeSupport, on_delete=models.CASCADE, default=1, verbose_name=_("Type support"))
    url = models.URLField(_("Url"), max_length=200, validators=[URLValidator()])
    requirements = models.TextField(_("Requirements"), default="")
    #id_educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = _("Support")
        verbose_name_plural = _("Supports")

    def __str__(self):
        return self.name
    
# Defines the model 'SupportForEducationalInstitution'
class SupportForEducationalInstitution(models.Model):
    id_support = models.ForeignKey(Support, on_delete=models.CASCADE, verbose_name=_("Support"))
    id_educationalInstitution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, verbose_name=_("Educational Institution"))

    class Meta:
        verbose_name = _("Type support Institution")
        verbose_name_plural = _("Type supports Institutions")

    
    
