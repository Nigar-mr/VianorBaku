from django.db import models
from tyres.models import Tyres
from generally.models import Client


class Card_list(models.Model):
    product = models.ForeignKey(Tyres, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    total_price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0, null=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name

    def session_user(self):
        return self.user.session_key


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def full_name(self):
        return self.first_name + self.last_name

class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='products')
    product_name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    total_price = models.PositiveIntegerField(null=True)

