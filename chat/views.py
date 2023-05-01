from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from chat.serializers import FindConnectionSerializer
from chat.models import ChatRoom
from user.models import User
from django.db.models import Q


# ! finds a chat connection
class FindConnectionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            connection_id = request.data.get("connection_id")
            user2 = User.objects.get(connection_id=connection_id)
            connection = FindConnectionSerializer(instance=user2).data

            if connection_id == f"{request.user.connection_id}":
                return Response(
                    {
                        "error": {
                            "message": "You are trying to connect with your own account.",
                            "status": "422"
                        }
                    }, status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )

            res1 = ChatRoom.objects.filter(
                Q(user1=request.user) & Q(user2=user2))

            res2 = ChatRoom.objects.filter(
                Q(user1=user2) & Q(user2=request.user))

            if res1 or res2:
                return Response({
                    "message": "already connected.", "data": {
                        "connection": connection,
                        "connected": True
                    }
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "connection found.", "data": {
                    "connection": connection,
                    "connected": False
                }
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                "error": {
                    "message": "No connection found with this Id",
                    "status": "404"
                }
            }, status=status.HTTP_404_NOT_FOUND)

        except ValueError:
            return Response({
                "error": {
                    "message": "Invalid id type.",
                    "status": "422"
                }
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({
                "error": {
                    "message": "Something went wrong!",
                    "status": "500"
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ! creates new chat connection
class CreateConnectionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            user2_id = request.data.get("user2_id")
            user2 = User.objects.get(pk=user2_id)

            res1 = ChatRoom.objects.filter(
                Q(user1=request.user) & Q(user2=user2))

            res2 = ChatRoom.objects.filter(
                Q(user1=user2) & Q(user2=request.user))

            if res1 or res2:
                return Response(
                    {"message": "already connected."}, status=status.HTTP_200_OK
                )

            room = ChatRoom.objects.create(user1=request.user, user2=user2)

            return Response(
                {"message": "connected successfully!"}, status=status.HTTP_200_OK
            )

        except User.DoesNotExist:
            return Response({
                "error": {
                    "message": "No user found!",
                    "status": "404"
                }
            }, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({
                "error": {
                    "message": "Something went wrong!",
                    "status": "500"
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
