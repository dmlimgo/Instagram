from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def post_image_path(post, filename):
    return f'posts/{post.pk}/images/{filename}'
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user.post_set.all() - 게시글인지? 좋아요한 글인지? 알수없다
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # 따라서 related_name을 추가해 헷갈리지 않게 해준다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    # image = models.ImageField()
    
    @property
    def like_count(self):
        return self.like_users.count()
    
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