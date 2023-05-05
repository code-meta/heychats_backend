from django.urls import path

from chat.consumers import ChatConsumer, ChatImageReceiverConsumer


ws_urlpatterns = [
    path("ws/chat/<uuid:sender>/<int:room_id>/",
         ChatConsumer.as_asgi(), name="chat_room"),
    path("ws/chat-image-receiver/<uuid:sender>/<int:room_id>/",
         ChatImageReceiverConsumer.as_asgi(), name="chat_room2"),
]
