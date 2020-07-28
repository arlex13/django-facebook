# rest framework
from rest_framework.generics import ListAPIView, CreateAPIView

from django.db.models import Count, Avg, Sum

# models
from users.models.posts import Post
from django.contrib.auth.models import User
# from users.models.users import User

# serializer
from users.serializers import post
# from users.serializers.user import AvgPostsSerializer


# ______________  private ______________


class MyPostsApiView(ListAPIView):
    serializer_class = post.MyPostsSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=1)


class MyAvgPostsApiView(ListAPIView):
    serializer_class = post.AvgPostsSerializer

    def get_queryset(self):

        result = User.objects.filter(
            id=1
        ).aggregate(
            avg_comment=Avg('user_post__total_comments'),
            avg_like=Avg('user_post__total_reactions')
        )
        return [result]


class PostsApiView(ListAPIView):
    serializer_class = post.PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class PostsAddApiView(CreateAPIView):
    serializer_class = post.PostAddSerializer
