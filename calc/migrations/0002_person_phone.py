# Generated by Django 2.2.4 on 2019-08-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
