from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def post_image_path(post, filename):
    return f'posts/{post.pk}/images/{filename}'
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
    file = models.ImageField(upload_to=post_image_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    thumbnail_fill = ProcessedImageField(
            upload_to=post_image_path,
            processors = [ResizeToFill(616, 616)],
            format = 'JPEG',
            options={'quality': 90},
        )