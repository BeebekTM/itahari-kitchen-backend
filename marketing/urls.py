from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogCategoryViewSet, BlogViewsSet, GalleryViewsSet, GalleryCategoryViewSet

router = DefaultRouter()

router.register(r'blog-categories', BlogCategoryViewSet)
router.register(r'blog', BlogViewsSet)
router.register(r'gallery-categories', GalleryCategoryViewSet)
router.register(r'gallary', GalleryViewsSet)

urlpatterns = [
    path('', include(router.urls)),
]
