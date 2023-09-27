from django.urls import path,include
from rest_framework import routers
from .views import RecommendationView

router = routers.DefaultRouter()

# Registramos las vistas
router.register(r'recommendation', RecommendationView)

urlpatterns = [
    path('', include(router.urls))
]

