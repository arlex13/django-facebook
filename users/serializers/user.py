from rest_framework import serializers

from users.models.posts import Post


class AvgPostsSerializer(serializers.Serializer):
    avg_comment = serializers.FloatField()
    avg_like = serializers.FloatField()
