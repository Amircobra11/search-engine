from django.db import models
from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

