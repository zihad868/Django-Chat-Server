from django.db import models
from django.conf import settings


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='received_messages'
    )
    receiver_group = models.ForeignKey(
        Group, null=True, blank=True, on_delete=models.CASCADE, related_name='group_messages'
    )
    message = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    file_expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Message from {self.sender}'

    class Meta:
        ordering = ['-timestamp']  # Latest messages first
