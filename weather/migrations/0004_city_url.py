# Generated by Django 3.2.15 on 2022-11-22 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_alter_about_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='url',
            field=models.SlugField(default='0', max_length=130),
        ),
    ]
