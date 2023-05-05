from django.contrib import admin

# Register your models here.

from chat.models import ChatRoom, TextMessage, ImageMessage


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ["user1", "user2", "room_id", "created_at"]


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    list_display = ["message", "sender", "room_id", "created_at"]

@admin.register(ImageMessage)
class ImageMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "sender", "room_id", "created_at"]
