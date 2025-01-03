from rest_framework import serializers

from infrastructure.persistence.models.messanger import ChatUser, Message
from infrastructure.persistence.models.user.user import User
from web.common.serializers import DateFieldDot


class MesageSerializer(serializers.ModelSerializer):
    time = DateFieldDot()
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ["user_id", "time", "id", "text"]

    def get_user_id(self, message):
        return message.chat_user.user_id


class InterlocutorSerializer(serializers.ModelSerializer):
    last_login = DateFieldDot()

    class Meta:
        model = User
        fields = ["full_name", "profile_picture", "last_login", "id"]


class ChatInterlocutorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = ChatUser
        fields = ["full_name", "profile_picture", "chat_id"]

    def get_full_name(self, chatuser):
        return chatuser.user.full_name

    def get_profile_picture(self, chatuser):
        return chatuser.user.profile_picture
