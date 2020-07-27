from rest_framework import serializers

from users.models.likes import Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
