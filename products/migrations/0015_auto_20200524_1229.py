# Generated by Django 3.0.6 on 2020-05-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200524_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_default.png', upload_to='products'),
        ),
    ]