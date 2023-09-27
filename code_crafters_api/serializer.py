from rest_framework import serializers
from .models import Recommendation, EducationalInstitution

# serializes the Recommendation model
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'


# serializes the EducationalInstitution model

