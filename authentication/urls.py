from django.urls import path
from authentication.views import CreateAccountView, UploadProfileView, LoginView


urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="create_account"),
    path("upload-profile/", UploadProfileView.as_view(), name="upload_profile"),
    path("login/", LoginView.as_view(), name="login"),
]
