# Generated by Django 5.1.2 on 2024-10-09 22:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='Nearby_Bus_Stops',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
