from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Sum
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    __phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[__phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=150)
    date_create_user = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'name: {self.name}, email: {self.email}, phone_number: {self.phone_number}, address: {self.address}'
    
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count =models.IntegerField()
    date_create_product = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'title: {self.title}, price: {self.price}, date: {self.date_create_product}'


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    date_create_order = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'user_id: {self.user}, total_cost: {self.total_cost}'
    
