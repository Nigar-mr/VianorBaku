from django.contrib import admin
from .models import Unique, FirstMenu, SubMenu, \
    SecondMenu, FooterMenu, FooterSubMenu, Newsletter, \
    Social, SocialText, ContactData, Phone, SlideImage, \
    LetterEmail, Client, FeaturedBlocks, Discount, DiscountProducts

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_key']

# Register your models here.

# empty_value_display = 'unknown'

class SubAdmin(admin.TabularInline):
    model = SubMenu
    extra = 2


class FSubAdmin(admin.TabularInline):
    model = FooterSubMenu
    extra = 5


class IconAdmin(admin.TabularInline):
    model = Social
    extra = 3


class PhoneAdmin(admin.TabularInline):
    model = Phone
    extra = 3

class DiscountProduct(admin.StackedInline):
    model = DiscountProducts
    extra = 1




# class NewsImg(admin.TabularInline):
#     model = NewsImg
#     extra = 1


@admin.register(Unique)
class UniqueAdmin(admin.ModelAdmin):
    list_display = ['logo', 'copiright']


@admin.register(SocialText)
class SocialAdmin(admin.ModelAdmin):
    inlines = [IconAdmin]
    list_display = ['description']


@admin.register(FirstMenu)
class FirstMenuAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SecondMenu)
class SecondMenuAdmin(admin.ModelAdmin):
    inlines = [SubAdmin]
    list_display = ['name']


@admin.register(FooterMenu)
class FooterMenuAdmin(admin.ModelAdmin):
    inlines = [FSubAdmin]
    list_display = ['name']


@admin.register(FooterSubMenu)
class FooterSubAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Newsletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(LetterEmail)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['email', 'create_date']
    readonly_fields = ['email']

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    inlines = [DiscountProduct]
    list_display = ['discount_name', 'percent', 'start_date', 'expiry_date']

# @admin.register(AboutUs)
# class AboutAdmin(admin.ModelAdmin):
#     list_display = ['text', 'create_date']
#
#
# @admin.register(DeliveryInfo)
# class DInfoAdmin(admin.ModelAdmin):
#     list_display = ['text', 'create_date']
#
#
# @admin.register(Privacy)
# class PrivacyAdmin(admin.ModelAdmin):
#     list_display = ['text', 'create_date']
#
#
# @admin.register(Terms)
# class TermsAdmin(admin.ModelAdmin):
#     list_display = ['text', 'create_date']
#

@admin.register(ContactData)
class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneAdmin]
    # list_display = ['name', '', 'phone']
    # date_hierarchy = 'create_date'


# @admin.register(ContactForm)
# class ContactMessages(admin.ModelAdmin):
#     list_display = ['name', 'email', 'enquiry', 'create_date']
#     readonly_fields = ['name', 'email', 'enquiry', 'create_date']


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     # inlines = [NewsImg]
#     list_display = ['context', 'text', 'imgname', 'publish_date']


@admin.register(SlideImage)
class SlideAdmin(admin.ModelAdmin):
    pass
    # list_display = ['image']

admin.site.register(FeaturedBlocks)
