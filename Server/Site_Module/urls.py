from django.urls import path
from Site_Module.views import *

urlpatterns = [
    path('', SiteSettingView.as_view(), name='site_setting_url')
]