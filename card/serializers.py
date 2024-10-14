from rest_framework import serializers
from .models import Card, DestinationCard
from accounts.models import User


class CardSerializer(serializers.ModelSerializer):
    passcode = serializers.CharField(write_only=True)
    owner = serializers.CharField(source="owner.phone", read_only=True)
    
    class Meta:
        model = Card
        fields = '__all__'
        
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