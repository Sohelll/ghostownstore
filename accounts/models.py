from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional 
    address = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=15)
    phone_num_2 = models.CharField(max_length=15, blank=True)

    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +'-'+ self.cart_product.title
    
