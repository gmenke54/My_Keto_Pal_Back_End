# Generated by Django 3.2 on 2022-02-07 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0002_auto_20220207_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='meal',
            new_name='meals',
        ),
    ]