import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat_room'  # Можно динамически передавать название комнаты
        self.room_group_name = f'chat_{self.room_name}'

        # Присоединение к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отключение от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Получение сообщения из WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data['content']

        # Сохранение сообщения в БД
        await self.save_message(content)

        # Отправка сообщения группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'content': content,
            }
        )

    # Отправка сообщения через WebSocket
    async def chat_message(self, event):
        content = event['content']
        await self.send(text_data=json.dumps({
            'content': content,
        }))

    async def save_message(self, content):
        from apps.chat.models import ChatMessage  # Импорт модели здесь, чтобы избежать циклических зависимостей
        await ChatMessage.objects.acreate(content=content)
