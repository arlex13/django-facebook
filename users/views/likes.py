# rest framework
from rest_framework.generics import CreateAPIView

# models
from users.models.likes import Like

# serializer
from users.serializers import likes


class LikeAddApiView(CreateAPIView):
    serializer_class = likes.LikeSerializer
