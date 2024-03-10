# Generated by Django 5.0.2 on 2024-03-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_purchase_is_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
