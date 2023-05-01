from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("ws connected...")

    async def receive_json(self, content, **kwargs):
        print("ws receive message...")
        print(content)

    async def disconnect(self, code):
        print("ws disconnected...", code)
        raise StopConsumer()
