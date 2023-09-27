from django.urls import path,include
from rest_framework import routers
from .views import RecommendationView, EducationalInstitutionSearchAPIView

router = routers.DefaultRouter()

# Registramos las vistas
router.register(r'recommendation', RecommendationView)

urlpatterns = [
    path('', include(router.urls)),
    path('educational_institutions/search/', EducationalInstitutionSearchAPIView.as_view(), name='educational_institution_search'),
]

