from django.contrib import admin
from .models import Recommendation, TypeSupport, Support

# Model registration for the administrator
admin.site.register(Recommendation)
admin.site.register(TypeSupport)
admin.site.register(Support)