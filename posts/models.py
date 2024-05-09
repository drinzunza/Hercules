from django.db import models
from users.models import CustomUser

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='media/posts', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-create_at"]
    
    
class PostReactions(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    heart = models.BooleanField(default=False)