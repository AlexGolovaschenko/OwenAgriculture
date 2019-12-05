# Generated by Django 2.2.5 on 2019-11-29 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='producttopic',
            options={'verbose_name': 'Категория продукта', 'verbose_name_plural': 'Категории продуктов'},
        ),
        migrations.AddField(
            model_name='producttopic',
            name='display_order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductTopic', verbose_name='Категория продукта'),
        ),
        migrations.AlterField(
            model_name='producttopic',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='producttopic',
            name='headline',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]