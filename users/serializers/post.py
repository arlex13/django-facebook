from rest_framework import serializers

from users.models.posts import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'description',
            'total_comments',
            'total_reactions'
        )
