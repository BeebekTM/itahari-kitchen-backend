from rest_framework import viewsets
from .models import Blog, BlogCategory, GalleryCategory, Gallery, Partner, Client, Offer
from .serializers import BlogSerializer, BlogCategorySerializer, GalleryCategorySerializer, GallerySerializer, PartnerSerializer, ClientSerializer, OfferSerializer
# Create your views here.

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all().order_by('-id')
    serializer_class = BlogCategorySerializer

class BlogViewsSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer

class GalleryCategoryViewSet(viewsets.ModelViewSet):
    queryset = GalleryCategory.objects.all().order_by('-id')
    serializer_class = GalleryCategorySerializer

class GalleryViewsSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-id')
    serializer_class = GallerySerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('-id')
    serializer_class = PartnerSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('-id')
    serializer_class = ClientSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer