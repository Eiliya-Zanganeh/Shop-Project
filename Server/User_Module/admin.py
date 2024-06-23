from django.contrib import admin
from User_Module.models import *


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    ...


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    ...
