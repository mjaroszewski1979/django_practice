from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)

class Order(models.Model):
    order_date = models.DateField(null=False)
    delivered_date = models.DateField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product, through='LineItem')

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
