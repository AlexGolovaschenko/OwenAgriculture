# Generated by Django 2.2.5 on 2019-12-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectarticle_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectarticle',
            name='image',
            field=models.ImageField(default=None, upload_to='project_images', verbose_name='Рисунок'),
        ),
    ]