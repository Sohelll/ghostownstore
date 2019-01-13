from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional 
    address = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=10)

    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username
