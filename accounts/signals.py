from django.db.models.signals import post_save
from .models import Wallet ,User


def create_wallet(sender, **kwargs):
    if kwargs['created']:
        Wallet.objects.create(user=kwargs['instance'], balance=0)
post_save.connect(receiver=create_wallet, sender=User)