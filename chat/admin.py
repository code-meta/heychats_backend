from django.contrib import admin

# Register your models here.

from chat.models import ChatRoom


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ["user1", "user2", "room_id", "created_at"]
