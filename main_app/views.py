from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dog
from .serializers import DogSerializer
from rest_framework import generics

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the dog-collector api home route!'}
    return Response(content)
  
class DogList(generics.ListCreateAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer
  lookup_field = 'id'

  
  
