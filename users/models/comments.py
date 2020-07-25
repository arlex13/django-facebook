# Django
from django.db import models

# Models
from .users import User
from .posts import Post


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content = models.CharField(max_length=255)

    def __str__(self):
        """Return Comment str representation."""
        return str(
            "DE--"+self.user.username +
            "--COMENTO--" + self.content +
            "--AL POST--" + self.post.description
        )
