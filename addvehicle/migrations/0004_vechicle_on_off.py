# Generated by Django 3.1.6 on 2022-01-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addvehicle', '0003_auto_20220118_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='vechicle',
            name='on_off',
            field=models.BooleanField(default=False),
        ),
    ]
