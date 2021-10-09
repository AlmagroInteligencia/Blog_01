from django.contrib import admin

# Register your models here.

from .models import Post, PostViewed, Comment, Like, DisLike, User

admin.site.register(Post)
admin.site.register(PostViewed)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(User)


