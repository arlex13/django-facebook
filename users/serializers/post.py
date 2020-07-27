from rest_framework import serializers

from rest_framework import serializers

from users.models.posts import Post

from users.serializers.user import UserSerializer


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

    class Meta:
        model = Post
        fields = (
            'id',
            'description',
            'user'
        )
        # fields = '__all__'
