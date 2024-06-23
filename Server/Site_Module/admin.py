from django.contrib import admin
from Site_Module.models import SiteSettingModel


@admin.register(SiteSettingModel)
class SiteSettingAdmin(admin.ModelAdmin):
    ...
