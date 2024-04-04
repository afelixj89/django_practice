from django.urls import path
from .views import Home, DogList, DogDetail, FeedingListCreate, FeedingDetail , ToyListCreate, ToyDetail, AddToyToDog, RemoveToyFromDog, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('dogs/', DogList.as_view(), name='dog-list'),
  path('dogs/<int:id>/', DogDetail.as_view(), name='dog-detail'),
  path('dogs/<int:dog_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('dogs/<int:dog_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
  path('dogs/<int:dog_id>/toys/', ToyListCreate.as_view(), name='toy-list-create'),
	path('dogs/<int:dog_id>/toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),
  path('dogs/<int:dog_id>/dog_toy/<int:toy_id>/', AddToyToDog.as_view(), name='add-toy-to-dog'),
  path('dogs/<int:dog_id>/remove_toy/<int:toy_id>/', RemoveToyFromDog.as_view(), name='remove-toy-from-dog'),
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh')

]

