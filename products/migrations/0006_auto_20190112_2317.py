# Generated by Django 2.1.2 on 2019-01-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
