from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import AuthenticationFailed
from .serializers import NoteSerializer
from accounts.models import User
from .models import Note

class NoteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):          
        user = request.user
        notes = Note.objects.filter(owner=user)
        ser = NoteSerializer(notes, many=True)
        return Response(ser.data)
        