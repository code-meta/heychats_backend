from django.urls import path
from authentication.views import CreateAccountView, UploadProfileView


urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="create_account"),
    path("upload-profile/", UploadProfileView.as_view(), name="upload_profile"),
]
