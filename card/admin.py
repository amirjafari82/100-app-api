from django.contrib import admin
from .models import Card, DestinationCard

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number','owner')
    list_filter = ('owner', 'card_number')
    
@admin.register(DestinationCard)
class DestinationCardAdmin(admin.ModelAdmin):
    list_display = ('card_number','card_owner','user')
    list_filter = ('card_owner', 'card_number', 'user')