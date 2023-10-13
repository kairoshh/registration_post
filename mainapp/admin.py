from django.contrib import admin

from mainapp.models import Post
from mainapp.models import Comment

admin.site.register(Post)
admin.site.register(Comment)
