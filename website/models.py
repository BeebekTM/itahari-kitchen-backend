from django.db import models
from django.utils.timezone import now

# Create your models here.
class ContactUs(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    businessType = models.TextField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


    def __str__(self):
        return self.fullName
