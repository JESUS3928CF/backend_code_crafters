from django.contrib import admin
from .models import Recommendation, TypeSupport, Support,TypeInstitute,EducationalInstitution

# Model registration for the administrator
admin.site.register(Recommendation)
admin.site.register(TypeSupport)
admin.site.register(Support)
admin.site.register(TypeInstitute)
admin.site.register(EducationalInstitution)

