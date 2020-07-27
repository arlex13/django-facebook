# rest framework
from rest_framework.generics import ListAPIView

# models
from users.models.posts import Post

# serializer
from users.serializers.post import PostListSerializer
from users.serializers.user import AvgPostsSerializer


class MyPostsApiView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=1)
