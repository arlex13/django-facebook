from django.db import models
from django.db.models import Count, Avg, Sum


class CommentManager(models.Manager):

    def list_comments(self, id_post):
        result = self.filter(
            post_id=id_post
        ).order_by('id')

        for r in result:
            print(r.content)
        return result


class PostManager(models.Manager):
    def AunNoUsado(self):
        return []


class UserManager(models.Manager):

    def average_comments_likes(self, id_user):
        result = self.filter(
            id=id_user
        ).aggregate(
            avg_comment=Avg('user_post__total_comments'),
            avg_like=Avg('user_post__total_reactions')
        )
        print(result)
        return result
