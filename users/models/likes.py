# Django
from django.db import models

# Models
from .users import User
from .posts import Post


class Like(model.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    like = models.BooleanField(default=True)

    def __str__(self):
        """Return post str representation."""
        return str(self.user + self.post + str(self.like))
