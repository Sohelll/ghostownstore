# Generated by Django 2.1.2 on 2019-01-12 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_photo_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo_1',
            new_name='photo_one',
        ),
    ]