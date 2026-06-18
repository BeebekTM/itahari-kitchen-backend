from django.contrib import admin
from .models import Blog, BlogCategory, Gallery, GalleryCategory

# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(BlogCategory, BlogCategoryAdmin)

class BLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'shortDescription',
        'fullContent',
        'category',
        'status',
        'tag',
    )

    list_filter = (
        'status',
        'category',
    )

    search_fields = (
        'title',
        'category',
    )

admin.site.register(Blog, BLogAdmin)

class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(GalleryCategory, GalleryCategoryAdmin)


class GalleryAdmin(admin.ModelAdmin):
        list_display = (
        'id',
        'category',
        'image',
    )

admin.site.register(Gallery, GalleryAdmin)
  