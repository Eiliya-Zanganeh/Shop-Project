from django.contrib import admin
from Site_Module.models import SiteSettingModel, BannerSiteModel


@admin.register(SiteSettingModel)
class SiteSettingAdmin(admin.ModelAdmin):
    ...


@admin.register(BannerSiteModel)
class BannerSiteAdmin(admin.ModelAdmin):
    ...
