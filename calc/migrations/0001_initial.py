# Generated by Django 2.2.4 on 2019-08-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
            ],
        ),
    ]
