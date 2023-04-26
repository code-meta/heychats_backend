from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import CreateUserSerialzier, CommonUserInfoSerializer, UploadProfileSerializer
from rest_framework import status
from services.token import get_tokens_for_user
from user.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# ! create new users
class CreateAccountView(APIView):
    def post(self, request, format=None):

        serializer = CreateUserSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = serializer.save()

            token = get_tokens_for_user(user)

            userInfo = CommonUserInfoSerializer(instance=user).data

            response_data = {
                "message": "User has created.",
                "data": {
                    "user": userInfo,
                    "token": token
                }
            }

            return Response(
                data=response_data,
                status=status.HTTP_201_CREATED
            )

        except:
            response_data = {
                "errors": {
                    "message": "something went wrong!",
                    "status": "500"
                }
            }

            return Response(
                data=response_data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# ! upload user's profile pictures
class UploadProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        serializer = UploadProfileSerializer(
            instance=request.user,
            data=request.FILES
        )

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response({"message": "profle picture has uploaded."}, status=status.HTTP_200_OK)

        except:
            return Response({
                "error": {
                    "message": "Something went wrong!",
                    "status": "500"
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
