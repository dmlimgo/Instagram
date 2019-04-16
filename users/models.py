from django.db import models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    