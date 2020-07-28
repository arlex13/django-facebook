# # rest framework
from rest_framework.generics import CreateAPIView


# # # models
# from users.models.users import User

# serializer
# from users.serializers import user
from users.serializers.user import UserSerializer


# # ______________  private ______________


# # ______________  public  ______________
class UserCreate(CreateAPIView):
    serializer_class = UserSerializer
