# Generated by Django 3.2 on 2021-05-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ph_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='pin_code',
            field=models.IntegerField(),
        ),
    ]
