from django.contrib import admin

from .models import Tyres, CarMarka, CarYear, CarModel, \
    CarMotor, TyresImage, Car, Brand
# from jet.filters import *

# Register your models here.

admin.site.empty_value_display = '(unknown)'

admin.site.register(CarMarka)
admin.site.register(CarModel)
admin.site.register(CarMotor)
admin.site.register(CarYear)
admin.site.register(Car)
admin.site.register(Brand)


# admin.site.register(OrderList)

class TyresImages(admin.TabularInline):
    model = TyresImage
    extra = 1



@admin.register(Tyres)
class TyresAdmin(admin.ModelAdmin):
    inlines = [TyresImages]
    list_display = ('id', 'name', 'price', 'published')
    list_filter = ('height', 'radius', 'published', 'width')
    search_fields = ('name',)
    list_editable = ('published',)



