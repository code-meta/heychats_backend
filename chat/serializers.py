from rest_framework import serializers
from user.models import User


class FindConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "profile"]
