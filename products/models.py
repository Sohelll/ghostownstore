from django.db import models
from datetime import datetime


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    photo_main_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    has_img = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category

    # def __id__(self):
    #     return self.id

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    product_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    feature_1 = models.CharField(max_length=400, blank=True)
    feature_2 = models.CharField(max_length=400, blank=True)
    feature_3 = models.CharField(max_length=400, blank=True)
    MRP = models.IntegerField()
    actual_price = models.IntegerField()
    delivery_charge = models.IntegerField()
    Warranty_info = models.CharField(max_length=200)
    photo_main_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_main_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

