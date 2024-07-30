
from django import forms
from .models import Product, UserSignUp


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserSignUp(forms.ModelForm):
    class Meta:
        model = UserSignUp
        fields = '__all__'