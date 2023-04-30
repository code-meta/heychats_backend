from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat.serializers import FindConnectionSerializer
from user.models import User


class FindConnectionView(APIView):
    def post(self, request, format=None):
        try:
            connection_id = request.data.get("connection_id")
            user = User.objects.get(connection_id=connection_id)
            connection = FindConnectionSerializer(instance=user).data

            return Response({
                "message": "connection found.", "data": {
                    "connection": connection
                }
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                "error": {
                    "message": "No connection found with this Id",
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
