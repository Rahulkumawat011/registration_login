from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField(null=True)
    product_quantity=models.IntegerField(null=True)
    product_description=models.CharField(max_length=100)



class UserSignUp(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    mobile=models.IntegerField(null=True)
    password=models.CharField(max_length=100)
