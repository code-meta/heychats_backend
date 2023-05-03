from django.urls import path
from chat.views import FindConnectionView, CreateConnectionView, ChatsView, ChatMessageView

urlpatterns = [
    path("find-chat-connection/",
         FindConnectionView.as_view(), name="find_connection"),
    path("create-connection/",
         CreateConnectionView.as_view(), name="create_connection"),
    path("all-chats/", ChatsView.as_view(), name="chats"),
    path("all-messages/", ChatMessageView.as_view(), name="messages"),
]
