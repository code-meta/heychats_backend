from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from user.models import User
import random
import uuid


def generate_room_id():
    return random.randint(1000000000, 9999999999)


class ChatRoom(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, auto_created=True)
    user1 = models.ForeignKey(
        User, related_name="user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(
        User, related_name="user2", on_delete=models.CASCADE)
    room_id = models.BigIntegerField(
        default=generate_room_id, auto_created=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.user1 == self.user2:
            raise ValidationError("user1 and user2 cannot be same")


class TextMessage(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, auto_created=True
    )
    sender = models.UUIDField()
    message = models.TextField()
    room_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class ImageMessage(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, auto_created=True
    )
    sender = models.UUIDField()
    image = models.ImageField(upload_to="uploads", blank=True)
    room_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
