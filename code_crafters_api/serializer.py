from rest_framework import serializers
from .models import Recommendation, EducationalInstitution, Support, TypeInstitute, TypeSupport

# serializes the Recommendation model
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'


# serializes the EducationalInstitution model
class EducationalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitution
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class TypeInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeInstitute
        fields = '__all__'

class TypeSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSupport
        fields = '__all__'




