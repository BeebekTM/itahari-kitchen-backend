from rest_framework import viewsets
from .models import Category, Brand, Product, ProductGallery, Order
from .serializers import (CategorySerializer, BrandSerializer, ProductSerializer, ProductGallerySerializer,
                          OrderSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('-id')
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category', 'brand').prefetch_related('gallery_images').order_by('-id')
    serializer_class = ProductSerializer

class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = ProductGallery.objects.select_related('product').order_by('-id')
    serializer_class = ProductGallerySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items").all()
    serializer_class = OrderSerializer