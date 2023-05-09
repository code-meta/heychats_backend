from django.urls import path
from authentication.views import CreateAccountView, UploadProfileView, LoginView, UserInfoView, UpdateUserProfile, DeleteUserAccount
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="create_account"),
    path("upload-profile/", UploadProfileView.as_view(), name="upload_profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("user-info/", UserInfoView.as_view(), name="user_info"),
    path('update-user-profile/', UpdateUserProfile.as_view(),
         name='update_user_profile'),
    path('delete-user/', DeleteUserAccount.as_view(),
         name='delete_user'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
