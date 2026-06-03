from django.contrib import admin
from .models import User, Brand, Category, Product, Inquiry, Order, OrderItem, BlogPost, GalleryItem

# This allows you to see the ordered items nested directly inside the order detail box
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'phone']
    inlines = [OrderItemInline] # Shows ordered products inside the order page

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created_at']

admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Inquiry)
admin.site.register(Order, OrderAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(GalleryItem)