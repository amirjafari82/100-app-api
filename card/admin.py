from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number','owner')
    list_filter = ('owner', 'card_number')