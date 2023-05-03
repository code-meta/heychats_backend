from django.core.exceptions import ValidationError
from django.contrib.auth.models import AnonymousUser


class JWTAuthMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])

        # print(headers.get(b"authorization").decode("utf-8"))

        scope['user'] = AnonymousUser()

        return await self.app(scope, receive, send)
