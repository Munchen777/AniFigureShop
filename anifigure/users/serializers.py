from rest_framework import serializers


from api.models import User
from api.utils import jwt_helper, encode_token


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ("id", "username", "email", "password",)
        extra_kwargs = {
        "password": {"write_only": True},
        "email": {"required": False},
        "username": {"required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=False)
    username = serializers.CharField(max_length=255, required=False)
    token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        # fields = [
        #     "email",
        #     "username",
        #     "password",
        # ]
        extra_kwargs = {
            "email": {"required": False},
            "username": {"required": False},
            "password": {"write_only": True, "required": False},
        }
        fields = UserSerializer.Meta.fields + ('token',)

    # def get_token(self, user):
    #     user = encode_token(user)
    #     return user
