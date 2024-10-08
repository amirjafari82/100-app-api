from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from .models import Image

class ImageView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        users = Image.objects.all()
        srz_data = UserSerializer(instance=users, many=True)
        return Response(srz_data.data,status.HTTP_200_OK)