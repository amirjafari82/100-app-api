from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CardSerializer, DesCardSerializer
from .models import Card, DestinationCard
from accounts.models import User


class CardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request):
        user = request.user
        card = Card.objects.filter(owner=user)
        if len(card) == 0:
            return Response({'message': 'You dont have any card', 'status': 'NoCard'})
        ser_data = CardSerializer(card, many=True)
        return Response({'message': 'success', 'data': ser_data.data})
    
class DesCardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request):
        user = request.user
        card = DestinationCard.objects.filter(user=user)
        if len(card) == 0:
            return Response({'message': 'You dont have any destination card', 'status': 'NoCard'})
        ser_data = DesCardSerializer(card, many=True)
        return Response({'message': 'success', 'data': ser_data.data})