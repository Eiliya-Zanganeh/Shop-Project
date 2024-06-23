from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from User_Module.serializer import UserSerializer, CartSerializer
from User_Module.models import UserModel, CartModel
from Product_Module.models import ProductModel
from Site_Module.models import SiteSettingModel
from Utils_Module.send_email import send_email
from django.conf import settings


class GetUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user
        data = UserSerializer(user)
        return Response(data.data, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    def post(self, request: Request):
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        is_user_exist: UserModel = UserModel.objects.filter(username=username).first()
        if not is_user_exist or not is_user_exist.is_active:
            if not is_user_exist:
                new_user = UserModel(
                    username=username,
                    first_name=first_name,
                    active_code=get_random_string(10),
                    is_active=False
                )
                new_user.set_password(password)
            else:
                new_user = is_user_exist
                new_user.active_code = get_random_string(10)
            new_user.save()
            site_setting: SiteSettingModel = SiteSettingModel.objects.filter(is_active=True).first()
            if site_setting.how_active_user_account == "email":
                send_email('فعالسازی حساب کاربری', new_user.username, 'email.html', {'user': new_user})
            elif site_setting.how_active_user_account == "phone":
                ...
                # Todo: Send SMS
            return Response("ok", status=status.HTTP_200_OK)
        else:
            return Response({"message": "user is exits"}, status=status.HTTP_400_BAD_REQUEST)


class ActivateAccountView(APIView):
    def get(self, request, email_active_code):
        if email_active_code == "":
            return redirect(settings.CLIENT_DOMAIN)
        else:
            user: UserModel = UserModel.objects.filter(active_code=email_active_code).first()
            if user:
                user.is_active = True
                user.active_code = ""
                user.save()
                return render(request, "success.html", {"client": settings.CLIENT_DOMAIN})
            else:
                return redirect(settings.CLIENT_DOMAIN)


class GetUserCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        cart = CartModel.objects.filter(user=request.user)
        cart_serializer = CartSerializer(cart, many=True)
        return Response(cart_serializer.data, status=status.HTTP_200_OK)


class AddCountCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        cart: CartModel = CartModel.objects.filter(id=pk).first()
        if cart.product.count > cart.count:
            cart.count += 1
            cart.save()
        return Response(cart.count, status=status.HTTP_200_OK)


class MinCountCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        cart: CartModel = CartModel.objects.filter(id=pk).first()
        if cart.count > 1:
            cart.count -= 1
            cart.save()
        return Response(cart.count, status=status.HTTP_200_OK)


class RemoveCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        cart: CartModel = CartModel.objects.filter(id=pk).first()
        cart.delete()
        return Response("OK", status=status.HTTP_200_OK)


class AddCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        is_define: CartModel = CartModel.objects.filter(user=request.user, product=pk).exists()
        if not is_define:
            product = ProductModel.objects.filter(id=pk).first()
            new_cart = CartModel(
                user=request.user,
                product=product
            )
            new_cart.save()
        return Response("OK", status=status.HTTP_200_OK)

