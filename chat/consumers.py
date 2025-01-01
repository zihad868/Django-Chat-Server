# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f'chat_{self.conversation_id}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the incoming message
        data = json.loads(text_data)
        message = data.get('message')
        sender = self.scope['user'].username  # Authenticated user

        # Broadcast the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
            }
        )

    async def chat_message(self, event):
        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))




from .models import Message

async def receive(self, text_data):
    data = json.loads(text_data)
    message = data.get('message')
    sender = self.scope['user']

    # Save the message
    Message.objects.create(
        sender=sender,
        receiver=None,  # Set the receiver (User or Group)
        group_id=self.conversation_id,  # Assuming this is a group chat
        message=message,
    )

    # Broadcast the message
    await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message,
            'sender': sender.username,
        }
    )
