# rest framework
from rest_framework.generics import ListAPIView


# models
from users.models.posts import Post
from users.models.users import User

# serializer
from users.serializers.post import PostListSerializer
from users.serializers.user import AvgPostsSerializer


class MyPostsApiView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=1)


class MyAvgPostsApiView(ListAPIView):
    serializer_class = AvgPostsSerializer

    def get_queryset(self):
        return User.objects.average_comments_likes(1)
