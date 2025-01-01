from django.urls import path
from .views import (
    ConversationMessagesView,
    SendMessageView,
    UserGroupsView,
    CreateGroupView,
    JoinGroupView,
    LeaveGroupView,
    FileMessageView,
)

urlpatterns = [
    path('api/messages/<int:conversation_id>/', ConversationMessagesView.as_view(), name='get_messages'),
    path('api/messages/<int:conversation_id>/send/', SendMessageView.as_view(), name='send_message'),
    path('api/groups/', UserGroupsView.as_view(), name='user_groups'),
    path('api/groups/create/', CreateGroupView.as_view(), name='create_group'),
    path('api/groups/<int:group_id>/join/', JoinGroupView.as_view(), name='join_group'),
    path('api/groups/<int:group_id>/leave/', LeaveGroupView.as_view(), name='leave_group'),
    path('api/messages/files/<int:file_id>/', FileMessageView.as_view(), name='file_message'),
]
