from rest_framework import serializers
from user.models import User
from services.validation import validate_password


class CreateUserSerialzier(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def validate(self, attrs):
        password = attrs.get("password")

        if password:
            instance = User(**attrs)
            validate_password(password, instance)

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CommonUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "profile", "connection_id", "about"]


class UploadProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile"]

    def update(self, instance, validated_data):
        instance.profile = validated_data.get("profile", instance.profile)
        instance.save()
        return instance

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "about"]

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.about = validated_data.get("about", instance.about)
        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]
