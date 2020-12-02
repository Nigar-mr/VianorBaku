from django.contrib import admin

from .models import Card_list, Order, OrderProducts


# # Register your models here.

class OrderProducts(admin.TabularInline):
    model = OrderProducts
    extra = 1


@admin.register(Card_list)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product', 'create_date', 'quantity', 'total_price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProducts]
    list_display = ['first_name', 'last_name', 'email', 'phone']

#
# # @admin.register(Order)
# # class OrderAdmin(admin.ModelAdmin):
# #     list_display = ['product', 'count', 'full_name', 'email', 'address', 'create_date']
# #     read_only_fields = ['product', 'count', 'full_name', 'email', 'address', 'create_date']
# #
# #
# # @admin.register(Wishlist)
# # class WishListAdmin(admin.ModelAdmin):
# #     list_display = ['product', 'create_date']
# #     readonly_fields = ['product', 'create_date']
# #
# #
# # @admin.register(ProductReturns)
# # class Return(admin.ModelAdmin):
# #     list_display = ['product', 'create_date']
# #     readonly_fields = ['product', 'create_date']
