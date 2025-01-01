from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Message, Group
from .serializers import MessageSerializer, GroupSerializer
from django.utils.timezone import now, timedelta


# Get messages in a conversation (paginated)
class ConversationMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, conversation_id):
        # Determine if it's a group or user conversation
        messages = Message.objects.filter(
            receiver_user_id=conversation_id, receiver_group=None
        ) | Message.objects.filter(receiver_group_id=conversation_id)

        page_size = 10
        page = int(request.query_params.get('page', 1))
        start = (page - 1) * page_size
        end = page * page_size
        paginated_messages = messages[start:end]

        serializer = MessageSerializer(paginated_messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Send a message (text or file)
class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, conversation_id):
        receiver_user = request.data.get('receiver_user')
        receiver_group = request.data.get('receiver_group')

        if receiver_user and receiver_group:
            return Response(
                {'error': 'Cannot send to both user and group at the same time.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        file = request.FILES.get('file')
        message = request.data.get('message', '')

        msg = Message.objects.create(
            sender=request.user,
            receiver_user_id=receiver_user,
            receiver_group_id=receiver_group,
            message=message,
            file=file,
            file_expiry=now() + timedelta(days=10) if file else None,
        )
        return Response(MessageSerializer(msg).data, status=status.HTTP_201_CREATED)


# Get all groups a user is part of
class UserGroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = request.user.groups.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create a new group
class CreateGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')
        if Group.objects.filter(name=name).exists():
            return Response({'error': 'Group name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        group = Group.objects.create(name=name)
        group.members.add(request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Join a group
class JoinGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        group.members.add(request.user)
        return Response({'message': 'Joined the group successfully.'}, status=status.HTTP_200_OK)


# Leave a group
class LeaveGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        group.members.remove(request.user)
        return Response({'message': 'Left the group successfully.'}, status=status.HTTP_200_OK)


# Retrieve a file message
class FileMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        message = get_object_or_404(Message, id=file_id, file__isnull=False)
        if message.file_expiry and message.file_expiry < now():
            return Response({'error': 'File has expired.'}, status=status.HTTP_410_GONE)

        return Response({'file_url': message.file.url}, status=status.HTTP_200_OK)
