from rest_framework import serializers
from .models import Dog, Feeding

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

class FeedingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeding
    fields = '__all__'
    read_only_fields = ('dog',)
