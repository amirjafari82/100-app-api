from rest_framework import serializers
from .models import Card, DestinationCard, LastSend, Transaction
from accounts.models import User


class CardSerializer(serializers.ModelSerializer):
    passcode = serializers.CharField(write_only=True)
    owner = serializers.SerializerMethodField(read_only=True)
    
    def get_owner(self,obj):
        user = User.objects.get(id=obj.owner.id)
        return f'{user.first_name} {user.last_name}'
    
    class Meta:
        model = Card
        fields = ('id','owner', 'card_number','passcode')
        

class CardBalanceSerialier(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_number','passcode','cvv2','exp')
    

        
class DesCardSerializer(serializers.ModelSerializer):
    card_owner = serializers.SerializerMethodField()
    card_owner_id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    
    def get_card_owner(self, obj):
        user = User.objects.get(id=obj.card_owner.id)
        return f'{user.first_name} {user.last_name}'
    
    def get_user_id(self,obj):
        user = User.objects.get(id=obj.user.id)
        return user.id
    
    def get_card_owner_id(self,obj):
        user = User.objects.get(id=obj.card_owner.id)
        return user.id
    
    def get_user(self, obj):
        user = User.objects.get(id=obj.user.id)
        return f'{user.first_name} {user.last_name}'
    
    class Meta:
        model = DestinationCard
        fields = '__all__'
        

class LastSendSerializer(serializers.ModelSerializer):
    to_firstname = serializers.SerializerMethodField()
    to_lastname = serializers.SerializerMethodField()
    to_image = serializers.SerializerMethodField()
    
    def get_to_firstname(self,obj):
        user = User.objects.get(id=obj.to_user.id)
        return user.first_name
    
    def get_to_lastname(self,obj):
        user = User.objects.get(id=obj.to_user.id)
        return user.last_name
    
    def get_to_image(self, obj):
        user = User.objects.get(id=obj.to_user.id)
        if user.image : return user.image.url
        return None
    
    class Meta:
        model = LastSend
        fields = '__all__'
        

class TransactionSerializer(serializers.ModelSerializer):
    des_card_num = serializers.SerializerMethodField()
    from_card_num = serializers.SerializerMethodField()
    
    def get_des_card_num(self, obj):
        des_card = obj.des_card
        if des_card : return des_card.card_number
        return None
    
    def get_from_card_num(self, obj):
        card = obj.card
        if card : return card.card_number
        return None

    
    class Meta:
        model = Transaction
        fields = '__all__'