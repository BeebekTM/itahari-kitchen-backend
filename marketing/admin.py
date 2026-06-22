from django.contrib import admin
from .models import (Blog, BlogCategory, Gallery, GalleryCategory, Partner,
                     Client, Offer, OfferPamphlets, Testimonial, Order, OrderItem)

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
  

class PartnerAdmin(admin.ModelAdmin):
     list_display = ('id','name','type','logo')

admin.site.register(Partner, PartnerAdmin)


class ClientAdmin(admin.ModelAdmin):
     list_display = ('id','name','type','logo')

admin.site.register(Client, ClientAdmin)


class OfferAdmin(admin.ModelAdmin):
     list_display = ('id','title','Description','validDate','offerImage')

admin.site.register(Offer, OfferAdmin)


class OfferPamphletsAdmin(admin.ModelAdmin):
    list_display = ('id','name','link','orderPriority','image')

admin.site.register(OfferPamphlets, OfferPamphletsAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','authorName','role','testimonialContent','profileImage')

admin.site.register(Testimonial, TestimonialAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fullName",
        "email",
        "phoneNumber",
        "total_amount",
        "created_at",
    )
    search_fields = (
        "fullName",
        "email",
        "phoneNumber",
    )
    readonly_fields = ("created_at",)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "productName",
        "quantity",
        "price",
    )
    search_fields = ("productName",)
admin.site.register(OrderItem, OrderItemAdmin)