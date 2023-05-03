from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer
from chat.models import TextMessage
from chat.serializers import TextMessageSerializer
from channels.db import database_sync_to_async
from datetime import datetime


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.room = str(self.scope["url_route"]["kwargs"]["room_id"])
        self.sender = str(self.scope["url_route"]["kwargs"]["sender"])
        await self.channel_layer.group_add(self.room, self.channel_name)
        print("ws connected...", self.room)

    async def receive_json(self, content, **kwargs):
        try:
            message_record = await database_sync_to_async(TextMessage)(
                message=content["message"],
                room_id=self.room,
                sender=self.sender,
                created_at=datetime.now()
            )

            await database_sync_to_async(message_record.save)()

            message = TextMessageSerializer(instance=message_record).data

            await self.channel_layer.group_send(self.room, {
                "type": "chat.message",
                "text": message
            })
        except:
            await self.send_json({"error": "something went wrong"})

    async def chat_message(self, event):
        await self.send_json({"message_content": event["text"]})

    async def disconnect(self, code):
        print("ws disconnected...", code)
        raise StopConsumer()
