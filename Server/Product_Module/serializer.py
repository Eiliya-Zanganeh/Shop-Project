from rest_framework import serializers
from Product_Module.models import ProductModel, ProductCategoryModel, GalleryModel


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    galleries = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = ProductModel
        fields = '__all__'
