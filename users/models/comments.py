# Django
from django.db import models
from django.db.models.signals import post_delete

# Models
from .users import User
from .posts import Post

# Managers
from users.managers import CommentManager


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content = models.CharField(max_length=255)

    objects = CommentManager()

    def __str__(self):
        """Return Comment str representation."""
        return str(
            "DE--"+self.user.username +
            "--COMENTO--" + self.content +
            "--AL POST--" + self.post.description
        )

    def save(self, *args, **kwargs):
        self.post.total_comments = self.post.total_comments + 1
        self.post.save()
        super(Comment, self).save(*args, **kwargs)


def remove_comment(sender, instance, **kwargs):
    instance.post.total_comments = instance.post.total_comments - 1
    instance.post.save()


post_delete.connect(remove_comment, sender=Comment)
