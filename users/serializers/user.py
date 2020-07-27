from rest_framework import serializers

from users.models.users import User


# ______________  private ______________


# ______________  public  ______________


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class UserAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'first_name',
            'username',
            'email',
            'phone',
        )
        # fields = '__all__'
