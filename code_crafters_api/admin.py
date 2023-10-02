from django.contrib import admin
from .models import *

# Models registration for the administrator
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('description', 'date') #Shows list of fields in the view
    search_fields = ('description', 'date') # search bar
    list_display_links = ('description',) #field for options (edit, delete, etc)

@admin.register(TypeSupport)
class TypeSupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') #Shows list of fields in the view
    search_fields = ('name', 'description') # Search in related fields
    list_display_links = ('name',) #field for options (edit, delete, etc)

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id_type_support', 'url', 'requirements') #Shows list of fields in the view
    search_fields = ('name', 'description', 'url', 'requirements') # Search in related fields
    list_display_links = ('name',) #field for options (edit, delete, etc)

@admin.register(TypeInstitute)
class TypeInstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') #Shows list of fields in the view
    search_fields = ('name', 'description') # Search in related fields
    list_display_links = ('name',) #field for options (edit, delete, etc)

@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'web_site', 'id_type_institute', 'location', 'id_support') #Shows list of fields in the view
    search_fields = ( 'id', 'name', 'web_site','location') # Search in related fields
    list_display_links = ('name',) #field for options (edit, delete, etc)

