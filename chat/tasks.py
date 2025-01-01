from celery import shared_task
from django.utils.timezone import now
from .models import Message

@shared_task
def delete_expired_files():
    expired_messages = Message.objects.filter(file_expiry__lte=now(), file__isnull=False)
    for message in expired_messages:
        if message.file:
            message.file.delete(save=False)  # Deletes the file from storage
            message.file = None
            message.save()
