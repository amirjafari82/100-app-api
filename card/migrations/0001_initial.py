# Generated by Django 5.1.1 on 2024-10-10 19:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, verbose_name='Card Number')),
                ('cvv2', models.CharField(max_length=6, verbose_name='CVV2')),
                ('exp', models.TimeField(verbose_name='Expire Date')),
                ('passcode', models.CharField(max_length=12, verbose_name='Passcode')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
