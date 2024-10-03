from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = UserSerializer(instance=users, many=True)
        return Response(srz_data.data,status.HTTP_200_OK)
        