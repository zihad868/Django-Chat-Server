from rest_framework import serializers
from .models import Message, Group

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver_user', 'receiver_group', 'message', 'file', 'timestamp']


class GroupSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'members']
