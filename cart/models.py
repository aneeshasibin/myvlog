from django.db import models
from shop.models import *
# Create your models here.
class cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='cart'
        ordering=['date_added']
    def __str__(self):
        return self.cart_id
class CartItem(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'

    def __str__(self):
        return self.product
    def total(self):
        return self.product.price*self.quantity