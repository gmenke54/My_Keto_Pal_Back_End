# Generated by Django 3.2 on 2022-02-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0008_auto_20220210_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
