# Generated by Django 5.0.2 on 2024-03-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='quantity_of_product',
            field=models.PositiveIntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
