from django.urls import path
from .views import Home, DogList, DogDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('dogs/', DogList.as_view(), name='dog-list'),
  path('dogs/<int:id>/', DogDetail.as_view(), name='dog-detail'),
]
