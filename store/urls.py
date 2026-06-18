from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet, BrandViewSet, ProductViewSet, ProductGalleryViewSet)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-gallery', ProductGalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]