# Generated by Django 3.0.5 on 2020-04-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=50, verbose_name='password of the user'),
        ),
    ]
