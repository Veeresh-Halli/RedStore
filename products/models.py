from django.db import models

# Create your models here.

class Products(models.Model):

  img = models.ImageField(upload_to='pics') 
  name = models.CharField(max_length=100)
  price = models.IntegerField()

class cartItems(models.Model):
  product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
  quantity = models.IntegerField(default=0)

  @property
  def get_total(self):
      total = self.product.price * self.quantity
      return total
  
  @property
  def get_cart_total(self):
      cart_total = self.get_total 
      return cart_total