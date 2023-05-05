from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer
from chat.models import TextMessage, ImageMessage
from chat.serializers import TextMessageSerializer, ImageMessageSerializer
from channels.db import database_sync_to_async
from datetime import datetime
from base64 import b64decode
from io import BytesIO
from django.core.files.images import ImageFile


# ! handles text messages
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

            message["type"] = "text"

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


# ! images data
class ChatImageReceiverConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.room_id = str(self.scope["url_route"]["kwargs"]["room_id"])
        self.sender = str(self.scope["url_route"]["kwargs"]["sender"])
        self.room = self.room_id + "-imessage"
        self.image_data = ""
        self.image_chunk_current_index = 0
        self.image_chunk_length = 0
        self.image_file_name = None
        await self.channel_layer.group_add(self.room, self.channel_name)
        print("ws image connected...", self.room)

    async def receive_json(self, content, **kwargs):
        self.image_data += content["image_chunk"]
        self.image_chunk_current_index = content["image_chunk_current_index"]
        self.image_chunk_length = content["image_chunk_length"]

        if self.image_file_name is None:
            self.image_file_name = content["image_file_name"]

        try:
            if self.image_chunk_current_index == self.image_chunk_length - 1:
                image_bytes = b64decode(self.image_data)

                image_file = BytesIO(image_bytes)

                image = ImageFile(image_file, self.image_file_name)

                record = await database_sync_to_async(ImageMessage)(
                    image=image,
                    room_id=self.room_id,
                    sender=self.sender,
                    created_at=datetime.now()
                )

                await database_sync_to_async(record.save)()

                image_message = ImageMessageSerializer(instance=record).data

                image_message["type"] = "image"

                await self.channel_layer.group_send(self.room, {
                    "type": "chat.imessage",
                    "text": image_message
                })

                self.image_data = ""
                self.image_chunk_current_index = 0
                self.image_chunk_length = 0
                self.image_file_name = None

        except:
            await self.send_json({"error": "something went wrong"})

    async def chat_imessage(self, event):
        await self.send_json({"message_content": event["text"]})

    async def disconnect(self, code):
        print("ws image disconnected...", code)
        raise StopConsumer()
 