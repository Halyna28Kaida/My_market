# Generated by Django 5.0.2 on 2024-03-10 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_purchase_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 10, 11, 45, 20, 956813, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='return',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 10, 11, 45, 20, 956813, tzinfo=datetime.timezone.utc)),
        ),
    ]
