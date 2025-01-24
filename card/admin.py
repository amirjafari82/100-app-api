from django.contrib import admin
from .models import Card, DestinationCard, LastSend, Transaction

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number','id','owner')
    list_filter = ('owner', 'card_number')
    
@admin.register(DestinationCard)
class DestinationCardAdmin(admin.ModelAdmin):
    list_display = ('card_number','card_owner','user', 'id')
    list_filter = ('card_owner', 'card_number', 'user')
    
@admin.register(LastSend)
class LastSendsAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user','amount')
    list_filter = ('from_user', 'to_user','amount', 'card', 'des_card')
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'created_at', 'status', 'refrence_number')
    search_fields = ('user__phone', 'refrence_number', 'issue_tracking', 'number')
    list_filter = ('user', 'type', 'created_at', 'status', 'refrence_number', 'issue_tracking', 'number')