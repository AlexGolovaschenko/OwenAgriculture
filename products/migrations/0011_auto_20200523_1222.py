# Generated by Django 3.0.6 on 2020-05-23 09:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20191211_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecificationField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50, verbose_name='Оглавление')),
                ('specification', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Спецификация продукта',
                'verbose_name_plural': 'Спецификации продуктов',
            },
        ),
        migrations.DeleteModel(
            name='ProductSpecification',
        ),
    ]
