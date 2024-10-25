from django.contrib import admin

from apps.cart.models import CartItem
# Register your models here.

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity')
    list_filter = ('id', 'quantity')