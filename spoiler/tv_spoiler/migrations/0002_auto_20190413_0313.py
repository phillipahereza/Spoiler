# Generated by Django 2.2 on 2019-04-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_spoiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='telephone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
