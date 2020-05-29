# Generated by Django 3.0.6 on 2020-05-28 13:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectarticle',
            name='header',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='projectarticle',
            name='short_description',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='projectarticle',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст'),
        ),
    ]