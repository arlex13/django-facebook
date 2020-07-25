from django.contrib import admin
from .models.posts import Post
from .models.likes import Like
from .models.comments import Comment
from .models.users import User

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(User)
