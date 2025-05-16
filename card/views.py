from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CardSerializer, DesCardSerializer, LastSendSerializer, TransactionSerializer, CardBalanceSerialier
from .models import Card, DestinationCard, Transaction
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
    
    
class TransferView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request):
        ser_data = LastSendSerializer(data=request.data)
        if ser_data.is_valid():
            amount = ser_data.validated_data['amount']
            card = ser_data.validated_data['card']
            des_card = ser_data.validated_data['des_card']
            if card.balance < amount:
                return Response({'message': 'Not Enough Money'}, status.HTTP_406_NOT_ACCEPTABLE)
            card.balance = card.balance - amount
            des_card.balance = des_card.balance + amount
            card.save()
            des_card.save()
            ser_data.save()
            Transaction.objects.create(user=request.user, type="Transfer", status="Successful", created_at="" , number=request.user.phone,amount=amount, card=card, des_card=des_card)
            return Response(ser_data.data)
        return Response({'message': 'failed'})
    
    
class LastSendsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request):
        user = request.user
        last_sends = user.from_user.all()
        ser_data = LastSendSerializer(last_sends, many=True)
        return Response(ser_data.data)
    

class TransactionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request):
        user = request.user
        data = request.data
        trans_type = data['type']
        match trans_type:
            case 'Transfer':
                ser_data = LastSendSerializer(data=data)
                if ser_data.is_valid():
                    amount = ser_data.validated_data['amount']
                    card = ser_data.validated_data['card']
                    des_card = ser_data.validated_data['des_card']
                    created_at = data['created_at']
                    if card == des_card:
                        return Response({'message': 'Card and Destination Card Can Not Be Same!'}, status.HTTP_406_NOT_ACCEPTABLE)
                    if card.balance < amount:
                        return Response({'message': 'Not Enough Money'}, status.HTTP_406_NOT_ACCEPTABLE)
                    if int(amount) < 1000:
                        return Response({'message': 'Not Acceptable Amount'}, status.HTTP_406_NOT_ACCEPTABLE)
                    card.balance = card.balance - amount
                    des_card.balance = des_card.balance + amount
                    card.save()
                    des_card.save()
                    ser_data.save()
                    Transaction.objects.create(user=user, type="Transfer", status="Successful", created_at=created_at , number=request.user.phone,amount=amount, card=card, des_card=des_card)
                    return Response(ser_data.data)
            case 'Recharge':
                card = Card.objects.get(id=data['card'])
                amount = data['amount']
                number = data['number']
                created_at = data['created_at']
                if card.balance < int(amount):
                    return Response({'message': 'Not Enough Money'}, status.HTTP_406_NOT_ACCEPTABLE)
                if int(amount) < 1000:
                    return Response({'message': 'Not Acceptable Amount'}, status.HTTP_406_NOT_ACCEPTABLE)
                Transaction.objects.create(user=user, type="Recharge", status="Successful", created_at=created_at, card=card, number=number, amount=amount)
                card.balance = card.balance - int(amount)
                card.save()
                return Response({'message': 'success'})
        
        return Response({'message': 'Unsupported Type'})
    
    def get(self, request: Request):
        user = request.user
        transactions = user.trans_user.all()
        ser_data = TransactionSerializer(transactions, many=True)
        return Response(ser_data.data)
        
        
class BalanceView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request):
        data = request.data['data']
        print(data['card_number'])
        try:
            card = Card.objects.get(card_number=data['card_number'])
            if (card.passcode != data['passcode']):
                return Response({'message': 'Passcode Is Wrong', 'field': 'Passcode', 'status': 406})
            if (card.cvv2 != data['cvv2']):
                return Response({'message': 'CVV2 Is Wrong', 'field': 'CVV2', 'status': 406})
            if (card.exp != data['exp']):
                return Response({'message': 'EXP Is Wrong', 'field': 'EXP', 'status': 406})
            balance = card.balance
            if(balance < 5000):
                return Response({'message': 'Your Balance is less than 5000IRT', 'status': 406})
            card.balance = card.balance - 144
            card.save()
            return Response({'message': 'success', 'balance': str(balance), 'status': 200}, status.HTTP_200_OK)
        except:
            return Response({'message': 'CardNumber Is Wrong', 'field': 'Card Number', 'status': 204})