# Django
from django.db import models
from django.db.models.signals import post_delete

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

    def save(self, *args, **kwargs):
        self.post.total_reactions = self.post.total_reactions + 1
        self.post.save()
        super(Like, self).save(*args, **kwargs)

    def __str__(self):
        return str(
            self.user.username +
            "--DIO--"+str(self.like) +
            "--al--" + self.post.description)


def remove_like(sender, instance, **kwargs):
    instance.post.total_reactions = instance.post.total_reactions - 1
    instance.post.save()


post_delete.connect(remove_like, sender=Like)
