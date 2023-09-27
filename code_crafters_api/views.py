# Imports needed to work with Django REST framework and Recommendation model.

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from django.db import models

from .serializer import RecommendationSerializer, EducationalInstitutionSerializer
from .models import Recommendation, EducationalInstitution

from rest_framework.generics import ListAPIView
from rest_framework.response import Response





# RecommendationView view definition.
# This view handles the operations related to recommendations.

class RecommendationView(viewsets.GenericViewSet):
    serializer_class = RecommendationSerializer 
    queryset = Recommendation.objects.all()

    # Método para manejar la creación de una nueva recomendación.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




class EducationalInstitutionSearchAPIView(ListAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = EducationalInstitutionSerializer

    filter_backend = [filters.SearchFilter]

    search_fields = ['name', 'location']