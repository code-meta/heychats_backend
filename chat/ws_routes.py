from django.urls import path

from chat.consumers import ChatConsumer


ws_urlpatterns = [
    path("ws/chat/<uuid:sender>/<int:room_id>/",
         ChatConsumer.as_asgi(), name="chat_room")
]
