from django.urls import path
from .views import HomeView, Filtered, CheckoutView, CartView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('filtered/', Filtered.as_view(), name='filtered'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart'),

]
