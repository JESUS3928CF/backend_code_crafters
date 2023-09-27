from rest_framework import serializers
from .models import Recommendation

# serializes the Recommendation model
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'