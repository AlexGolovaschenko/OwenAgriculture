# Generated by Django 3.0.6 on 2021-07-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200528_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Показывать'),
        ),
    ]
