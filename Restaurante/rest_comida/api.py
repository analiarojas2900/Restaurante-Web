from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UserAPI(APIView):
    def post(self,request):
        serializers = UserSerializer( data = request.data)
        if serializers.is_valid():
            user = serializers.save()