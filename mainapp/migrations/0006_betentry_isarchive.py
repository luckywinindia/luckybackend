# Generated by Django 4.0.3 on 2022-10-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_betentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='betentry',
            name='isArchive',
            field=models.BooleanField(default=False),
        ),
    ]