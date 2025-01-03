import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user_id = self.scope["user"].id

        self.group_name = f"user_{user_id}"

        async_to_sync(self.channel_layer.group_add)(f"user_{user_id}", self.channel_name)

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "chat_message", "message": message})

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "chat", "message": message}))

    def channel_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))


class SendAlertConsumer(WebsocketConsumer):
    def connect(self):
        user_id = self.scope["url_route"]["kwargs"]["user_id"]
        user_notification_id = self.scope["url_route"]["kwargs"]["user_notification_id"]

        # self.group_name = f"user_{user_id}"

        # async_to_sync(self.channel_layer.group_add)(f"user_{user_id}", self.channel_name)

        from notifications.serializers import UserNotificationSerializer

        from infrastructure.persistence.models.notifications import UserNotification

        channel_layer = self.channel_layer
        group_name = f"user_{user_id}"

        user_alert = UserNotification.objects.get(id=user_notification_id)
        message = UserNotificationSerializer(user_alert).data

        async_to_sync(channel_layer.group_send)(group_name, {"type": "chat.message", "message": message})

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "chat_message", "message": message})

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "chat", "message": message}))

    def channel_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
