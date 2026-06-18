from django.contrib import admin
from .models import Category, Brand, Product, ProductGallery


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'productName',
        'category',
        'brand',
        'price',
        'quantity',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'category',
        'brand',
        'created_at',
    )

    search_fields = (
        'productName',
        'description',
        'brand__name',
        'category__name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    inlines = [ProductGalleryInline]

admin.site.register(Product, ProductAdmin)

class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'image',
    )
    search_fields = (
        'product__productName',
    )
admin.site.register(ProductGallery, ProductGalleryAdmin)