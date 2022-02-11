# Generated by Django 3.2 on 2022-02-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0011_profile_daily_carb'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='daily_fat',
            field=models.IntegerField(default=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='daily_sugar',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='daily_carb',
            field=models.IntegerField(default=30),
        ),
    ]