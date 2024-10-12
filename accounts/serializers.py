from rest_framework import serializers
from accounts.models import User, Wallet


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ("phone","password","first_name","last_name")
        
    def create(self, validated_data):
        user = User(
            phone = validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("phone", "first_name", "last_name", "is_admin")