from rest_framework import status, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from Site_Module.models import SiteSettingModel

from Product_Module.serializer import ProductSerializer, ProductCategorySerializer
from Product_Module.models import ProductCategoryModel, ProductModel


class PopularProductsView(APIView):
    def get(self, request: Request):
        popular_products = ProductModel.objects.filter(offer__gt=0, count__gt=0).order_by('-id')[:10]
        popular_products_serializer = ProductSerializer(popular_products, many=True)
        return Response(popular_products_serializer.data, status=status.HTTP_200_OK)


class ProductCategoryView(APIView):
    def get(self, request: Request):
        category_list = ProductCategoryModel.objects.all()
        category_serializer = ProductCategorySerializer(category_list, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)


class NewProductView(APIView):
    def get(self, request: Request):
        product_list = ProductModel.objects.filter(count__gt=0).order_by('-id')[:10]
        product_serializer = ProductSerializer(product_list, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)


class BuyCountProductView(APIView):
    def get(self, request: Request):
        product_list = ProductModel.objects.filter(count__gt=0).order_by('-buy_count', '-id')[:10]
        product_serializer = ProductSerializer(product_list, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)


class VisitCountProductView(APIView):
    def get(self, request: Request):
        product_list = ProductModel.objects.filter(count__gt=0).order_by('-visits', '-id')[:10]
        product_serializer = ProductSerializer(product_list, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)


class ProductWithCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return ProductModel.objects.filter(category=self.kwargs['pk'], count__gt=0).order_by('-id')


class SpecialProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return ProductModel.objects.filter(offer__gt=0, count__gt=0).order_by('-id')


class DetailProductView(APIView):
    def get(self, request: Request, pk):
        product: ProductModel = ProductModel.objects.prefetch_related('galleries').filter(pk=pk).first()
        product.visits += 1
        product.save()
        suggested_products = ProductModel.objects.filter(category=product.category, count__gt=0)[:10]
        product_serializer = ProductSerializer(product, many=False)
        suggested_products_serializer = ProductSerializer(suggested_products, many=True)
        return Response(
            {
                "product": product_serializer.data,
                "suggested_products": suggested_products_serializer.data
            },
            status=status.HTTP_200_OK
        )
