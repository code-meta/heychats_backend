from django.urls import path
from authentication.views import CreateAccountView


urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="create_account")
]
