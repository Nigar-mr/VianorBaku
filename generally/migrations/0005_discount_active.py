# Generated by Django 3.1.2 on 2020-11-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generally', '0004_auto_20201105_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]