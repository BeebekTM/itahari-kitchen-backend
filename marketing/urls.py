from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (BlogCategoryViewSet, BlogViewsSet, GalleryViewsSet, GalleryCategoryViewSet,
                    PartnerViewSet, ClientViewSet, OfferViewSet, OfferPamphletsViewSet, TestimonialViewSet)

router = DefaultRouter()

router.register(r'blog-categories', BlogCategoryViewSet)
router.register(r'blog', BlogViewsSet)
router.register(r'gallery-categories', GalleryCategoryViewSet)
router.register(r'gallary', GalleryViewsSet)
router.register(r'partner', PartnerViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'offerpamphlets', OfferPamphletsViewSet)
router.register(r'testimonials', TestimonialViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
