# rest framework
from rest_framework.generics import CreateAPIView


# # models
from users.models.users import User

# # serializer
from users.serializers import user


# ______________  private ______________


# ______________  public  ______________

class UsersAddApiView(CreateAPIView):
    serializer_class = user.UserAddSerializer
