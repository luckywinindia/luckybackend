# Generated by Django 4.0.3 on 2022-09-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Manager'), (3, 'Broker'), (4, 'User')], default=4),
        ),
    ]
