# Generated by Django 2.1 on 2020-12-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_exercise',
            field=models.DateField(blank=True, default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='account',
            name='no_consecutive_day',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
