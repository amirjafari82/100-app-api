from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    passcode = serializers.CharField(write_only=True)
    
    class Meta:
        model = Card
        fields = '__all__'