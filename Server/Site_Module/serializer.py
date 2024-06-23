from rest_framework import serializers
from Site_Module.models import SiteSettingModel


class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettingModel
        fields = '__all__'