from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/product/category')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Brand Category"
        verbose_name_plural = "Brand Category"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/brand')
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brand"

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        ('In Stock','in_stock'),
        ('Low Stock','low_stock' ),
        ('Out Of Stock','out_of_stock'),
    ]

    productName = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Stock')
    description = models.TextField(blank=True)
    keyFeatures = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/product')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.status = 'out_of_stock'
        elif self.quantity <= 5:
            self.status = 'low_stock'
        else:
            self.status = 'in_stock'

        if not self.slug:
            base_slug = slugify(self.productName)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

        
    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.productName


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='media/product/productGallery')

    class Meta:
        verbose_name = "Product Gallery"
        verbose_name_plural = "Product Gallery"

    def __str__(self):
        return self.product.productName