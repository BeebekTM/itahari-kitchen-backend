from rest_framework import serializers
from .models import Category, Brand, Product, ProductGallery


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)
    gallery_images = ProductGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'