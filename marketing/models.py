from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Category"

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = [('Draft', 'in_draft,'),
                     ('Published','in_published')]
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    shortDescription = models.TextField()
    fullContent = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Published')
    image = models.ImageField(upload_to='Media/Blog/Category')
    tag = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Blogs"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Category"

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='Media/Gallery')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.category