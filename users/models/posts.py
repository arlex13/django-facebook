# Django
from django.db import models

# Models
from .users import User


class Post(model.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(
        max_length=700, help_text=('The description must have a maximum of 700 characters'))

    def __str__(self):
        """Return post str representation."""
        return str(self.user + self.content)
