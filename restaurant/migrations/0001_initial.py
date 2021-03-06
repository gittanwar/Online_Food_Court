# Generated by Django 3.2 on 2021-05-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=50)),
                ('r_town', models.CharField(max_length=50)),
                ('r_mobile', models.IntegerField()),
                ('r_pass', models.CharField(default='ADMIN', max_length=12)),
                ('r_email', models.EmailField(max_length=50)),
                ('r_image', models.ImageField(blank=True, null=True, upload_to='restaurant/')),
                ('r_license', models.ImageField(blank=True, null=True, upload_to='restaurant/license')),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]
