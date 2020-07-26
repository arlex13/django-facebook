from django.db import models


class CommentManager(models.Manager):

    def list_comments(self, id_post):
        result = self.filter(
            post_id=id_post
        ).order_by('id')

        for r in result:
            print(r.content)
        return result
