from rest_framework import serializers
from Site_Module.models import SiteSettingModel, BannerSiteModel


class BannerSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerSiteModel
        fields = '__all__'


class SiteSettingSerializer(serializers.ModelSerializer):
    banners = BannerSiteSerializer(many=True, read_only=True)

    class Meta:
        model = SiteSettingModel
        fields = '__all__'
