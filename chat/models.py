from django.db import models
from django.utils.timezone import now
from datetime import timedelta

from authentication.models import CustomUser

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(CustomUser, related_name="groups")


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name="received_messages")
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE, related_name="group_messages")
    message = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="uploads/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    file_expiry = models.DateTimeField(default=lambda: now() + timedelta(days=10))


    def is_file_expired(self):
        return now() > self.file_expiry