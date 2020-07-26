# Django
from django.db import models

# Models
from .users import User


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(
        max_length=700, help_text=('The description must have a maximum of 700 characters'))

    total_comments = models.PositiveIntegerField(default=0)
    total_reactions = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return post str representation."""
        return str(self.user.username +
                   "--PUBLICO--" + self.description +
                   "--Total de comentarios--" + str(self.total_comments) +
                   "--Total de reacciones--" + str(self.total_reactions)

                   )
