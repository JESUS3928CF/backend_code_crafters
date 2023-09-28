from django.urls import path,include
from rest_framework import routers
from .views import RecommendationView, EducationalInstitutionSearchView, SupportForEducationalInstitutionAPIView

router = routers.DefaultRouter()

# Registramos las vistas
router.register(r'recommendation', RecommendationView)

urlpatterns = [
    path('', include(router.urls)),
    path('educational_institutions/search/', EducationalInstitutionSearchView.as_view(), name='educational_institution_search'),
    path('supports/', SupportForEducationalInstitutionAPIView.as_view()),
] 

