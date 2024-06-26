from django.contrib import admin
from Product_Module.models import *


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'offer_price', 'offer']
    list_filter = ['category']
    list_editable = ['price']


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    ...


@admin.register(LightAndBrightnessModel)
class LightAndBrightnessAdmin(admin.ModelAdmin):
    ...
