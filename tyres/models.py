from django.db import models
# from django_countries.fields import CountryField

from django.contrib.contenttypes.fields import GenericRelation
from .helps import orded_status


# from star_ratings.models import Rating


# Create your models here.
class CarMarka(models.Model):
    marka = models.CharField(max_length=50, verbose_name='Marka')

    def __str__(self):
        return self.marka


class CarModel(models.Model):
    marka = models.ForeignKey(CarMarka, on_delete=models.CASCADE, verbose_name='Marka')
    model = models.CharField(max_length=50, verbose_name='Model')

    def __str__(self):
        return self.model


class CarMotor(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Model')
    motor = models.CharField(max_length=50, verbose_name='Motor')

    def __str__(self):
        return self.motor


class CarYear(models.Model):
    motor = models.ForeignKey(CarMotor, on_delete=models.CASCADE, verbose_name='Motor')
    year = models.PositiveIntegerField(verbose_name='İl')

    def __str__(self):
        return str(self.year)


class Car(models.Model):
    marka = models.ForeignKey(CarMarka, on_delete=models.CASCADE, null=True, verbose_name='Maşının Markası')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True, verbose_name='Maşının Modeli')
    motor = models.ForeignKey(CarMotor, on_delete=models.CASCADE, null=True, verbose_name='Maşının Motoru')
    car_year = models.ForeignKey(CarYear, on_delete=models.CASCADE, null=True, verbose_name='Maşının İli')

    def __str__(self):
        return self.marka.marka + ' ' + self.model.model + ' ' + self.motor.motor


class Brand(models.Model):
    brand = models.CharField(max_length=64, verbose_name='Brend')
    img = models.ImageField(upload_to='brand/', null=True)

    def __str__(self):
        return self.brand


class Tyres(models.Model):
    car = models.ManyToManyField(Car)
    # category = models.IntegerField(choices=Category)
    width = models.CharField(max_length=64, verbose_name='En (mm)')
    height = models.CharField(max_length=64, verbose_name='Hündürluk (%)')
    radius = models.CharField(max_length=64, verbose_name='Radius (düym)')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    klass = models.CharField(max_length=64, verbose_name='Klass')
    price = models.FloatField(verbose_name='Qiymət')
    year = models.PositiveIntegerField(verbose_name='İl')
    country = models.CharField(max_length=64, verbose_name='Ölkə')
    name = models.CharField(max_length=128, verbose_name='Ad')
    published = models.BooleanField(default=False, verbose_name='published')

    def __str__(self):
        return self.name


class TyresImage(models.Model):
    trye = models.ForeignKey(Tyres, on_delete=models.CASCADE, verbose_name='Təkərin')
    images = models.ImageField(upload_to='tyres/', verbose_name='Şəkil')

    def __str__(self):
        return self.trye.name

    def get_image(self):
        return self.images

# class OrderList(models.Model):
#     product = models.ForeignKey(Tyres, on_delete=models.CASCADE)
#     # add_to_card = models.BooleanField(default=False)
#     total_price = models.PositiveIntegerField(default=0)
#     quantity = models.PositiveIntegerField(default=0, null=True)
#     # total_list = models.PositiveIntegerField(default=0)
#     create_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.product.name
