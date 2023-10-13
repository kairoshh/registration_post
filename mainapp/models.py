from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='post/images')
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name='posts'
    )

    is_draft = models.BooleanField(default=False)

    

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
    to=User, on_delete=models.CASCADE,
    related_name='comments'
    )
    post = models.ForeignKey(
    to=Post, on_delete=models.CASCADE,
    related_name='comments'
    )
    