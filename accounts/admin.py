from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Wallet


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "is_admin"]

class WalletInline(admin.StackedInline):
    model = Wallet
    can_delete = False

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["phone", "first_name", "last_name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["phone"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone", "first_name", "last_name"],
            },
        ),
    ]
    search_fields = ["phone", "first_name", "last_name"]
    ordering = ["phone"]
    filter_horizontal = []
    inlines = (WalletInline,)
    

admin.site.register(User, UserAdmin)