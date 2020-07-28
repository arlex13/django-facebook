from rest_framework import serializers

from users.models.posts import Post
from users.models.comments import Comment

from users.serializers.user import UserSerializer
from users.serializers.comments import CommentSerializer


# ______________  private ______________

class AvgPostsSerializer(serializers.Serializer):
    avg_comment = serializers.FloatField()
    avg_like = serializers.FloatField()


class MyPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'description',
            'total_comments',
            'total_reactions'
        )


# ______________  PUBLIC  ______________

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments_post = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'description',
            'user',
            'comments_post'
        )

    def get_comments_post(self, obj):
        query = Comment.objects.list_comments(obj.id)
        comments_serializado = CommentSerializer(query, many=True).data
        return comments_serializado


class PostAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'description',
            'user'
        )
