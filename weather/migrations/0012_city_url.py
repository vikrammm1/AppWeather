# Generated by Django 3.2.15 on 2022-11-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0011_remove_city_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='url',
            field=models.SlugField(default=0, max_length=130),
            preserve_default=False,
        ),
    ]
