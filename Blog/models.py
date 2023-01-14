from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Blogpost'
        verbose_name_plural = 'Blogposts'

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title + ' / ' + self.content

    def first_image(self):
        image = BlogImage.objects.filter(blogpost=self)
        if (image):
            return image.first()
        return None


class BlogImage(models.Model):
    blogpost = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogpost_pictures/', blank=True, null=True)

    def __str__(self):
        return self.product.title + " | Url: " + self.image.url
