from django.db import models
from django.utils.text import slugify

# Create your models here.



# blog_category

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# blog_post

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True, null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title



class AboutUs(models.Model):
    content = models.TextField()