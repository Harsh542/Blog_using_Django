from django.utils import timezone
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.TextField(unique=True)
    slug = models.SlugField(unique=True)
    intro = models.TextField(max_length=100)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,null=True)
    name = models.TextField()
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name