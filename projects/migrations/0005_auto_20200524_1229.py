# Generated by Django 3.0.6 on 2020-05-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20191210_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectarticle',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects', verbose_name='Рисунок'),
        ),
    ]