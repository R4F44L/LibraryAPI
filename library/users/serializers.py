from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()

    def validate(self, data):
        if data.get("email"):
            u = User.objects.filter(email=data.get("email")).first()
            if u:
                raise(serializers.ValidationError)
        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        u = User.objects.create(**validated_data)
        validated_data.pop("password")
        return validated_data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({"is_superuser": self.user.is_superuser})
        print(data)
        return data
