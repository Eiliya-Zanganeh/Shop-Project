from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from Site_Module.models import SiteSettingModel
from Site_Module.serializer import SiteSettingSerializer


class SiteSettingView(APIView):
    def get(self, request: Request):
        site_setting = SiteSettingModel.objects.filter(is_active=True).first()
        site_setting_serializer = SiteSettingSerializer(site_setting)
        return Response(site_setting_serializer.data, status=status.HTTP_200_OK)