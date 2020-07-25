# Django
from django.db import models

# Models
from .users import User
from .posts import Post


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    like = models.BooleanField(default=True)

    class Meta:
        # que solo pueda existir un like al mismo post del mismo user
        unique_together = ('user', 'post')

    def __str__(self):
        return str(
            self.user.username +
            "--DIO--"+str(self.like) +
            "--al--" + self.post.description
        )
