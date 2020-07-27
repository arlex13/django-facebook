# rest framework
from rest_framework.generics import CreateAPIView

# models
from users.models.comments import Comment

# serializer
from users.serializers import comments


class CommentAddApiView(CreateAPIView):
    serializer_class = comments.CommentSerializer
