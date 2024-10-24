from django.contrib import admin

from apps.products.models import (Products, ProductImage, ProductsFeature,
                                  BigCategory, Category, ProductReview)
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

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')

@admin.register(BigCategory)
class BigCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')