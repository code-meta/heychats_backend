from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import CreateUserSerialzier, CommonUserInfoSerializer, UploadProfileSerializer, UserLoginSerializer, UpdateUserProfileSerializer
from rest_framework import status
from services.token import get_tokens_for_user
from user.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


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
            return Response({"message": "profle picture has uploaded.", "data": serializer.data}, status=status.HTTP_200_OK)

        except:
            return Response({
                "error": {
                    "message": "Something went wrong!",
                    "status": "500"
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ! login view
class LoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            return Response(
                {
                    "non_field_errors": ["Invalid user credentials!"]
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        token = get_tokens_for_user(user)

        userInfo = CommonUserInfoSerializer(instance=user).data

        return Response(
            {
                "message": "logged in successfully!",
                "data": {
                    "token": token,
                    "user": userInfo
                }
            },
            status=status.HTTP_200_OK
        )


# ! returns basic user informations
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        userInfo = CommonUserInfoSerializer(instance=request.user).data

        return Response(
            {
                "message": "basic user informations!",
                "data": {
                    "user": userInfo
                }
            },
            status=status.HTTP_200_OK
        )


# ! update user profile
class UpdateUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        serializer = UpdateUserProfileSerializer(
            instance=request.user,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response({"message": "User profile is updated.", "data": serializer.data}, status=status.HTTP_200_OK)

        except:
            return Response({
                "error": {
                    "message": "Something went wrong!",
                    "status": "500"
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
