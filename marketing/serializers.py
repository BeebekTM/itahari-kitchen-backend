from rest_framework import serializers
from .models import (Blog, BlogCategory, Gallery, GalleryCategory, Partner, Client,
                     Offer, OfferPamphlets, Testimonial)

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

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class OfferPamphletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferPamphlets
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

