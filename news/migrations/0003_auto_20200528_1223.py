# Generated by Django 3.0.6 on 2020-05-28 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200528_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата публикации'),
        ),
    ]
