from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the dogs_are_better api home route!'}
    return Response(content)
