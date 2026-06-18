from django.contrib import admin
from .models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(ContactUs, ContactUsAdmin)
