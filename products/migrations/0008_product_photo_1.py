# Generated by Django 2.1.2 on 2019-01-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_photo_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]