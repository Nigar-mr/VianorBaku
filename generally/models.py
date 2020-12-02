from django.db import models
from djrichtextfield.models import RichTextField
from tyres.models import Tyres


class Client(models.Model):
    session_key = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Unique(models.Model):
    logo = models.ImageField(upload_to='main/', verbose_name='Logo')
    copiright = models.CharField(max_length=300, verbose_name='Copyright')


class FeaturedBlocks(models.Model):
    name = models.CharField(max_length=25)
    value = models.CharField(max_length=25)


class FirstMenu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SlideImage(models.Model):
    desktop_image = models.ImageField(upload_to='slide/')
    mobile_image = models.ImageField(upload_to='slide/')

    def get_image(self):
        return self.desktop_image.url


class SecondMenu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    menu = models.ForeignKey(SecondMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FooterMenu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FooterSubMenu(models.Model):
    menu = models.ForeignKey(FooterMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.menu.name


class Newsletter(models.Model):
    # menu = models.ForeignKey(FooterMenu, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=255)

    create_date = models.DateTimeField(auto_now_add=True)


class LetterEmail(models.Model):
    email = models.CharField(max_length=50)

    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email


class SocialText(models.Model):
    description = models.CharField(max_length=100)


class Social(models.Model):
    text = models.ForeignKey(SocialText, on_delete=models.CASCADE, null=True)
    icon = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    create_date = models.DateTimeField(auto_now_add=True)


class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=24)
    location = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=100)

    create_date = models.DateTimeField(auto_now_add=True)


class Phone(models.Model):
    name = models.ForeignKey(ContactData, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    enquiry = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    context = models.CharField(max_length=300)
    text = RichTextField()
    images = models.ImageField(upload_to='news/')
    imgname = models.CharField(max_length=255)

    publish_date = models.DateTimeField(auto_now_add=True)


class ViewingNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    viewing = models.IntegerField()


class Discount(models.Model):
    active = models.BooleanField(default=True)
    discount_name = models.CharField(max_length=50)
    percent = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()

    def __str__(self):
        return self.discount_name


class DiscountProducts(models.Model):
    diccount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    products = models.ForeignKey(Tyres, related_name='product',  on_delete=models.CASCADE)

    def __str__(self):
        return self.products

    def get_price(self):
        return self.products.price

# class AboutUs(models.Model):
#     text = models.TextField()
#
#     create_date = models.DateTimeField(auto_now_add=True)
#
#
# class DeliveryInfo(models.Model):
#     text = models.TextField()
#
#     create_date = models.DateTimeField(auto_now_add=True)
#
#
# class Privacy(models.Model):
#     text = models.TextField()
#
#     create_date = models.DateTimeField(auto_now_add=True)
#
#
# class Terms(models.Model):
#     text = models.TextField()
#
#     create_date = models.DateTimeField(auto_now_add=True)
#


# class TestDrive(models.Model):
#     context = models.CharField(max_length=300)
#     text = RichTextField()
#     images = models.ImageField(upload_to='testdrive/')
#     imgname = models.CharField(max_length=255)
#     tags = models.CharField(max_length=300, blank=True)
#
#     create_date = models.DateTimeField(auto_now_add=True)
#
#
# class ViewingTest(models.Model):
#     test = models.ForeignKey(TestDrive, on_delete=models.CASCADE)
#     viewing = models.IntegerField()
