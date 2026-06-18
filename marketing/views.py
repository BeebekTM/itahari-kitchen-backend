from rest_framework import viewsets
from .models import Blog, BlogCategory, GalleryCategory, Gallery
from .serializers import BlogSerializer, BlogCategorySerializer, GalleryCategorySerializer, GallerySerializer
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
