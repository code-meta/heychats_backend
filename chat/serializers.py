from rest_framework import serializers
from user.models import User
from chat.models import TextMessage


class FindConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "profile"]


class CommonUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "profile"]


class TextMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMessage
        fields = "__all__"
