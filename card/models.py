from django.db import models
from accounts.models import User
from django.core.validators import MinLengthValidator


class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_card')
    card_number = models.CharField(verbose_name="Card Number", max_length=16, unique=True)
    cvv2 = models.CharField(verbose_name="CVV2", max_length=6)
    exp = models.CharField(verbose_name='Expire Date',max_length=10)
    balance = models.PositiveBigIntegerField(verbose_name="Balance", default=0)
    passcode = models.CharField(verbose_name="Passcode", max_length=12)
    
    def __str__(self):
        return f'{self.card_number} {self.owner}'
    

class DestinationCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='des_card_user', default=None)
    card_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='des_card_owner', default=None)
    card_number = models.CharField(verbose_name="Card Number", max_length=16, validators=[MinLengthValidator(16)], unique=True)