# Generated by Django 3.1.2 on 2020-11-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyres', '0003_tyres_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='img',
            field=models.ImageField(null=True, upload_to='brand/'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=64, verbose_name='Brend'),
        ),
    ]
