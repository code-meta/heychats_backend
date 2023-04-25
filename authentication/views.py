from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import CreateUserSerialzier, CommonUserInfoSerializer
from rest_framework import status
from services.token import get_tokens_for_user


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
