# Generated by Django 3.2 on 2022-02-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0003_rename_meal_food_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
