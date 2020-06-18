# Generated by Django 3.0.6 on 2020-06-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('banner_image', models.ImageField(upload_to='banners', verbose_name='Картинка баннера')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок отображения')),
                ('display', models.BooleanField(default=True, verbose_name='Показывать')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]
