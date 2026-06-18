from rest_framework import serializers
from .models import Blog, BlogCategory, Gallery, GalleryCategory

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Blog
        fields = '__all__'

class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Gallery
        fields = '__all__'