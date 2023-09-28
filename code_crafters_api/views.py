# Imports needed to work with Django REST framework and Recommendation model.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import models

from .serializer import RecommendationSerializer, EducationalInstitutionSerializer, SupportSerializer, TypeInstituteSerializer, TypeSupportSerializer
from .models import Recommendation, EducationalInstitution, Support, TypeInstitute, TypeSupport

from rest_framework.response import Response
from rest_framework import generics

from rest_framework.generics import ListAPIView








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



class EducationalInstitutionSearchView(generics.ListAPIView):
    serializer_class = EducationalInstitutionSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = EducationalInstitution.objects.filter(name__icontains=keyword)
        else:
            queryset = EducationalInstitution.objects.all()
        return queryset




class SupportForEducationalInstitutionAPIView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        id_educational_institution = self.request.query_params.get('id_educational_institution')
        id_type_support = self.request.query_params.get('id_type_support')

        if id_educational_institution:
            queryset = queryset.filter(id_educational_institution=id_educational_institution)

        if id_type_support:
            queryset = queryset.filter(id_type_support=id_type_support)

        return queryset



class TypeInstituteViewSet(viewsets.ModelViewSet):
    queryset = TypeInstitute.objects.all()
    serializer_class = TypeInstituteSerializer

    def get(self, request):
        return Response(self.queryset.values())
    
class TypeSupportViewSet(viewsets.ModelViewSet):
    queryset = TypeSupport.objects.all()
    serializer_class = TypeSupportSerializer

    def get(self, request):
        return Response(self.queryset.values())


