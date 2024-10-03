from .models import Image
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'