from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from restaurant.views import (AuthViewSet, BrandViewSet, CategoryViewSet, ProductViewSet, 
                              InquiryViewSet, OrderViewSet, BlogPostViewSet, GalleryItemViewSet)

# 1. Initialize the router
router = DefaultRouter()

# 2. Register ALL routes BEFORE passing them to urlpatterns
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'inquiries', InquiryViewSet, basename='inquiry')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'blog', BlogPostViewSet, basename='blog')
router.register(r'gallery', GalleryItemViewSet, basename='gallery')

# 3. Build the URL patterns using the fully loaded router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# 4. Handle media asset routing for product images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)