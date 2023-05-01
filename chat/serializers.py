from rest_framework import serializers
from user.models import User
from chat.models import ChatRoom


class FindConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "profile"]

