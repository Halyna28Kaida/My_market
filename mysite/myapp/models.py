from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class MyUser(AbstractUser):
    purse = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, upload_to="images")
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    buyer = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    quantity_of_product = models.PositiveIntegerField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)


class Return(models.Model):
    text = models.TextField(blank=True, null=True)
    purchase_for_returning = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

