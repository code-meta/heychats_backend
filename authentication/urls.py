from django.urls import path
from authentication.views import CreateAccountView, UploadProfileView, LoginView, UserInfoView
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView


urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="create_account"),
    path("upload-profile/", UploadProfileView.as_view(), name="upload_profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("user-info/", UserInfoView.as_view(), name="user_info"),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
