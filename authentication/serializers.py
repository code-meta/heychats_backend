from rest_framework import serializers
from user.models import User
from django.contrib.auth.password_validation import validate_password


class CreateUserSerialzier(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CommonUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UploadProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile"]

    def update(self, instance, validated_data):
        instance.profile = validated_data.get("profile", instance.profile)
        instance.save()
        return instance
