from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField()
    
    def __str__(self):
        return f'Post : {self.pk}'
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.pk])
        
class Image(models.Model):
    file = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)