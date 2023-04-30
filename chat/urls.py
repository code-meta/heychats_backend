from django.urls import path
from chat.views import FindConnectionView


urlpatterns = [
    path("find-chat-connection/",
         FindConnectionView.as_view(), name="find_connection")
]
