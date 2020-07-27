# rest framework
from rest_framework.generics import ListAPIView, CreateAPIView

# models
from users.models.posts import Post
from users.models.users import User

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
        return User.objects.average_comments_likes(1)


# ______________  public  ______________


class PostsApiView(ListAPIView):
    serializer_class = post.PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class PostsAddApiView(CreateAPIView):
    serializer_class = post.PostAddSerializer
