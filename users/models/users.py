"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


# Managers
from users.managers import UserManager


class User(AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone = models.CharField(
        'phone', max_length=11,
        null=True, blank=True,
        help_text=('The number must have 8 digits')
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address'
    )

    objects = UserManager()

    def __str__(self):
        """Return username."""
        return str(str(self.id) + " "+self.username)
