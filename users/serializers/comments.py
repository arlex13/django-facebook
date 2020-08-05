from rest_framework import serializers

from users.models.comments import Comment


from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = (
            'id',
            'content',
            'user',
        )


class CommentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
