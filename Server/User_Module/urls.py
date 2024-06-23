from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from User_Module.views import *

urlpatterns = [
    path('', GetUser.as_view(), name="get_user_url"),
    path('token/', TokenObtainPairView.as_view(), name='token_url'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_url'),
    path('register/', RegisterUser.as_view(), name='register_url'),
    path('activate-account/<email_active_code>', ActivateAccountView.as_view(), name='activate_account_url'),
    path('cart/', GetUserCartView.as_view(), name='cart_url'),
    path('add-count-cart/<pk>/', AddCountCartView.as_view(), name='add_count_cart_url'),
    path('min-count-cart/<pk>/', MinCountCartView.as_view(), name='min_count_cart_url'),
    path('remove-cart/<pk>/', RemoveCartView.as_view(), name='remove_cart_url'),
    path('add-cart/<int:pk>/', AddCartView.as_view(), name='add_cart_url'),
]
