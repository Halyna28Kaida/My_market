from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Purchase, Return, MyUser
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']


class ProductCreateForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'quantity']


class PurchaseCreateForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity_of_product']


class ReturnForm(ModelForm):
    class Meta:
        model = Return
        fields = ['text', 'purchase_for_returning']

