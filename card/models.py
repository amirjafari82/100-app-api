from django.db import models
from accounts.models import User
from django.core.validators import MinLengthValidator
import random

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
    

class LastSend(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user', default=None)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user', default=None)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card', default=None)
    des_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='des_card', default=None)
    amount = models.PositiveBigIntegerField(verbose_name="Amount", default=0)
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trans_user', default=None)
    type = models.CharField(choices=(
        ("Recharge", ("Recharge")),
        ("Internet", ("Internet")),
        ("Receive Money", ("Receive Money")),
        ("Transfer", ("Transfer")),
    ), max_length=50, blank=True, null=True)
    status = models.CharField(choices=(
        ("Successful", ("Successful")),
        ("Failed", ("Failed")),
    ), max_length=50, blank=True, null=True)
    created_at = models.CharField(verbose_name="Date and Time", max_length=100)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='trans_card', default=None, null=True)
    des_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='trans_des_card', default=None, null=True, blank=True)
    number = models.CharField(verbose_name="Number", max_length=11)
    issue_tracking = models.CharField(unique=True, verbose_name="Issue Tracking", max_length=12)
    refrence_number = models.CharField(unique=True, verbose_name="Refrence No", max_length=12)
    amount = models.PositiveBigIntegerField(verbose_name="Amount", default=0)
    
    
    def save(self, *args, **kwargs):
        if not self.issue_tracking and not self.refrence_number:
            self.issue_tracking = random.randrange(100000000000,999999999999)
            self.refrence_number = random.randrange(100000000000,999999999999)
        
        super().save(*args, **kwargs)