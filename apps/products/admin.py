from django.contrib import admin

from apps.products.models import Products, ProductImage, ProductsFeature
# Register your models here.

class ImageTabularInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class FeatureTabularInline(admin.TabularInline):
    model = ProductsFeature
    extra = 2

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    inlines = (ImageTabularInline, FeatureTabularInline)
